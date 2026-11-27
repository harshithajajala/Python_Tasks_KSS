"""
PROJECT TITLE: Railway Gauges Data Analytics

DESCRIPTION:
This project analyzes railway gauge data
using Python data analytics libraries.

OBJECTIVE:
To analyze Broad Gauge, Metre Gauge,
Narrow Gauge and Total values over the years.

DATASET: railway_gauges.csv

SCENARIOS:
1. Basic Data Loading and Cleaning
2. Simple Visualization - Line Graph
3. Filtering and Grouped Bar Chart
4. Feature Engineering and Pie Chart
5. Advanced Analysis and Multiple Graphs
"""

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# Create Graphs folder
os.makedirs("Graphs", exist_ok=True)


# SCENARIO 1: DATA LOADING AND CLEANING

# Load railway dataset
df = pd.read_csv("railway_gauges.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Display first five records
print("\nFirst Five Records:")
print(df.head())

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())

# Identify missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df = df.fillna(0)

# Support either Metre or Meter spelling
if "Metre Gauge" not in df.columns and "Meter Gauge" in df.columns:
    df.rename(columns={"Meter Gauge": "Metre Gauge"}, inplace=True)

# Convert gauge columns into numeric values
gauge_columns = [
    "Broad Gauge",
    "Metre Gauge",
    "Narrow Gauge",
    "Total"
]

for col in gauge_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

# Display dataset information
print("\nDataset Information:")
df.info()

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

print("\nScenario 1 Completed Successfully!")


# SCENARIO 2: SIMPLE VISUALIZATION - LINE GRAPH

# Extract Year and Total columns
data = df[["Year", "Total"]]

print("\nYear and Total Tracks:")
print(data)

# Create line graph
plt.figure(figsize=(12, 6))

plt.plot(
    data["Year"],
    data["Total"],
    marker="o",
    label="Total Tracks"
)

plt.title("Total Railway Tracks Over Years")
plt.xlabel("Year")
plt.ylabel("Total Railway Tracks")

plt.xticks(rotation=90)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save graph
plt.savefig("Graphs/total_tracks_line.png")

plt.show()

# Identify overall trend
if df["Total"].iloc[-1] > df["Total"].iloc[0]:
    print("Overall Trend: Increasing")
elif df["Total"].iloc[-1] < df["Total"].iloc[0]:
    print("Overall Trend: Decreasing")
else:
    print("Overall Trend: No Overall Change")


# SCENARIO 3: FILTERING AND GROUPED BAR CHART

# Extract starting year
df["Start_Year"] = df["Year"].astype(str).str[:4].astype(int)

# Filter years after 2000
recent_data = df[df["Start_Year"] > 2000].copy()

# Select gauge columns
gauge_data = recent_data[
    ["Year", "Broad Gauge", "Metre Gauge", "Narrow Gauge"]
]

print("\nRailway Data After 2000:")
print(gauge_data)

# Create grouped bar chart
gauge_data = gauge_data.set_index("Year")

gauge_data.plot(
    kind="bar",
    figsize=(12, 6),
    width=0.8
)

plt.title("Railway Gauge Comparison After 2000")
plt.xlabel("Year")
plt.ylabel("Track Length")

plt.legend(title="Gauge Type")
plt.xticks(rotation=45)
plt.tight_layout()

# Save graph
plt.savefig("Graphs/gauge_comparison_bar.png")

plt.show()

# Identify dominant gauge
print("\nTotal of Each Gauge After 2000:")

gauge_totals_recent = recent_data[
    ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
].sum()

print(gauge_totals_recent)

print("\nDominant Gauge:", gauge_totals_recent.idxmax())


# SCENARIO 4: FEATURE ENGINEERING AND PIE CHART

# Calculate total of each gauge
gauge_totals = df[
    ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
].sum()

print("\nTotal of Each Gauge:")
print(gauge_totals)

# Create new DataFrame
gauge_df = pd.DataFrame({
    "Gauge": gauge_totals.index,
    "Total": gauge_totals.values
})

print("\nGauge DataFrame:")
print(gauge_df)

# Create pie chart
plt.figure(figsize=(8, 8))

plt.pie(
    gauge_df["Total"],
    labels=gauge_df["Gauge"],
    autopct="%1.1f%%",
    startangle=90,
    explode=(0.1, 0, 0)
)

plt.title("Percentage Contribution of Railway Gauges")

plt.tight_layout()

# Save graph
plt.savefig("Graphs/gauge_contribution_pie.png")

plt.show()

# Find highest contributing gauge
print("\nHighest Contributing Gauge:")
print(gauge_totals.idxmax())


# SCENARIO 5: ADVANCED ANALYSIS

# Create percentage columns
df["% Broad Gauge"] = (
    df["Broad Gauge"] / df["Total"].replace(0, np.nan)
) * 100

df["% Metre Gauge"] = (
    df["Metre Gauge"] / df["Total"].replace(0, np.nan)
) * 100

df["% Narrow Gauge"] = (
    df["Narrow Gauge"] / df["Total"].replace(0, np.nan)
) * 100

# Replace invalid percentage values
percentage_columns = [
    "% Broad Gauge",
    "% Metre Gauge",
    "% Narrow Gauge"
]

df[percentage_columns] = df[percentage_columns].fillna(0)

print("\nPercentage Composition:")
print(df[["Year"] + percentage_columns].round(2))


# Calculate yearly growth using NumPy
total = df["Total"].to_numpy()

growth = np.diff(total)

print("\nYearly Growth:")
print(growth)

# Find highest yearly growth
max_growth_index = np.argmax(growth)

print("\nHighest Yearly Growth:")
print("From Year:", df["Year"].iloc[max_growth_index])
print("To Year:", df["Year"].iloc[max_growth_index + 1])
print("Growth:", growth[max_growth_index])

# Identify overall gauge decline
print("\nGauge Decline Analysis:")

for col in ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]:

    if df[col].iloc[-1] < df[col].iloc[0]:
        print(col, "has decreased overall")

    else:
        print(col, "has increased overall")


# GRAPH 4: PERCENTAGE COMPOSITION LINE GRAPH

plt.figure(figsize=(12, 6))

plt.plot(
    df["Year"],
    df["% Broad Gauge"],
    marker="o",
    label="Broad Gauge"
)

plt.plot(
    df["Year"],
    df["% Metre Gauge"],
    marker="o",
    label="Metre Gauge"
)

plt.plot(
    df["Year"],
    df["% Narrow Gauge"],
    marker="o",
    label="Narrow Gauge"
)

plt.title("Railway Gauge Percentage Composition")
plt.xlabel("Year")
plt.ylabel("Percentage (%)")

plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save graph
plt.savefig("Graphs/gauge_percentage_line.png")

plt.show()


# GRAPH 5: STACKED BAR CHART

plt.figure(figsize=(14, 7))

df.set_index("Year")[
    ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
].plot(
    kind="bar",
    stacked=True,
    figsize=(14, 7)
)

plt.title("Railway Gauge Composition")
plt.xlabel("Year")
plt.ylabel("Track Length")

plt.xticks(rotation=90)
plt.legend(title="Gauge Type")
plt.tight_layout()

# Save graph
plt.savefig("Graphs/gauge_composition_stacked.png")

plt.show()


