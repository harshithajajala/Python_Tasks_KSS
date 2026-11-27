# Combined Visualization Dashboard sales = np.array([100, 200, 150, 300]) 
# products = ["A", "B", "C", "D"].Create DataFrame 
# Plot: 
# Line graph (trend) 
# Bar chart (comparison) 
# Pie chart (distribution) 
# Show all in single figure (subplots)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create sales data
sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]

# Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

print(df)

# Create a single figure with three subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 1. Line graph - Sales trend
axes[0].plot(df["Product"], df["Sales"], marker="o")
axes[0].set_title("Sales Trend")
axes[0].set_xlabel("Products")
axes[0].set_ylabel("Sales")
axes[0].grid(True)

# 2. Bar chart - Sales comparison
axes[1].bar(df["Product"], df["Sales"])
axes[1].set_title("Sales Comparison")
axes[1].set_xlabel("Products")
axes[1].set_ylabel("Sales")

# 3. Pie chart - Sales distribution
axes[2].pie(
    df["Sales"],
    labels=df["Product"],
    autopct="%1.1f%%"
)
axes[2].set_title("Sales Distribution")

# Adjust spacing and display all graphs
plt.tight_layout()
plt.show()
