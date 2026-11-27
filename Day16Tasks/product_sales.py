# Product Sales Bar Chart.products = ["Pen", "Book", "Pencil"],sales = np.array([50, 80, 40])  
# Create DataFrame.Plot bar chart 
# Add labels and title


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Product names and sales
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])

# Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

print(df)

# Plot bar chart
plt.figure(figsize=(7, 5))
plt.bar(df["Product"], df["Sales"])

# Add labels and title
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales Bar Chart")

plt.show()
