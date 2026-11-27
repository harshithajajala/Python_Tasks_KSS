# Monthly Sales Line Graph.A shop records monthly sales:sales = np.array([100, 150, 200, 250, 300]) months = ["Jan", "Feb", "Mar", "Apr", "May"] 
# Convert data into a Pandas DataFrame 
# Plot a line graph 
# Label X-axis as months and Y-axis as sales


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Monthly sales data
sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]

# Convert data into DataFrame
df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

# Display DataFrame
print(df)

# Plot line graph
plt.figure(figsize=(8, 5))
plt.plot(df["Month"], df["Sales"], marker='o')

# Add labels and title
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Line Graph")

# Display graph
plt.grid(True)
plt.show()
