# Data Cleaning + Visualization  data = np.array([100, np.nan, 200, 150, np.nan, 300]). Convert to Pandas Series 
# Replace NaN with mean 
# Plot: 
# Line graph of cleaned data 
# Bar chart of values > average


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data with missing values
data = np.array([100, np.nan, 200, 150, np.nan, 300])

# Convert NumPy array into Pandas Series
series = pd.Series(data)

print("Original Data:")
print(series)

# Calculate mean (NaN values are ignored)
average = series.mean()

# Replace NaN values with mean
cleaned_data = series.fillna(average)

print("Cleaned Data:")
print(cleaned_data)

print("Average:", average)

# Filter values greater than average
filtered_data = cleaned_data[cleaned_data > average]

# Create two subplots in one figure
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 1. Line graph of cleaned data
axes[0].plot(cleaned_data.index, cleaned_data, marker="o")
axes[0].set_title("Cleaned Data Line Graph")
axes[0].set_xlabel("Index")
axes[0].set_ylabel("Values")
axes[0].grid(True)

# 2. Bar chart of values greater than average
axes[1].bar(filtered_data.index, filtered_data)
axes[1].set_title("Values Above Average")
axes[1].set_xlabel("Index")
axes[1].set_ylabel("Values")

# Display both graphs
plt.tight_layout()
plt.show()
