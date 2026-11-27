# Filtered Bar Chart marks = np.array([45, 80, 60, 30, 90]) 
# names = ["A", "B", "C", "D", "E"] 
# Convert to DataFrame 
# Filter students with marks > 50 
# Plot bar chart only for filtered students


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Student names and marks
marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

# Create DataFrame
df = pd.DataFrame({
    "Student": names,
    "Marks": marks
})

print("Original Data:")
print(df)

# Filter students with marks greater than 50
filtered_df = df[df["Marks"] > 50]

print("Filtered Data:")
print(filtered_df)

# Plot filtered bar chart
plt.figure(figsize=(7, 5))
plt.bar(filtered_df["Student"], filtered_df["Marks"])

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students Scoring Above 50")

plt.show()
