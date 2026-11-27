# Multi-Line Graph for Sales Comparison data = { "Month": ["Jan", "Feb", "Mar"], "Store_A": [100, 150, 200], "Store_B": [90, 140, 210] } 
# Create DataFrame 
# Plot two line graphs on same plot 
# Add legend


import pandas as pd
import matplotlib.pyplot as plt

# Store sales data
data = {
    "Month": ["Jan", "Feb", "Mar"],
    "Store_A": [100, 150, 200],
    "Store_B": [90, 140, 210]
}

# Create DataFrame
df = pd.DataFrame(data)

print(df)

# Plot two line graphs
plt.figure(figsize=(8, 5))

plt.plot(df["Month"], df["Store_A"], marker="o", label="Store A")
plt.plot(df["Month"], df["Store_B"], marker="o", label="Store B")

# Add labels, title and legend
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales Comparison Between Stores")
plt.legend()
plt.grid(True)

plt.show()
