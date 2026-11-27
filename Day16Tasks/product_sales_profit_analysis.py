# Product Sales & Profit Analysis.sales = np.array([200, 300, 250, 400, 350]) .profit = np.array([50, 70, 60, 90, 80]) .products = ["A", "B", "C", "D", "E"] 
# sales = np.array([200, 300, 250, 400, 350]).profit = np.array([50, 70, 60, 90, 80]) .products = ["A", "B", "C", "D", "E"] .Create DataFrame .Line graph → sales trend 
# Bar chart → product vs sales .Pie chart → sales contribution .Histogram → profit distribution .Scatter plot → sales vs profit.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({
    "Product": products,
    "Sales": sales,
    "Profit": profit
})

print("Product Sales and Profit Data:")
print(df)

plt.figure(figsize=(7, 5))
plt.plot(products, sales, 'ro-', label="Sales")
plt.title("Product Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(7, 5))
plt.bar(products, sales, color='blue')
plt.title("Product-wise Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()
plt.figure(figsize=(6, 6))
plt.pie(
    sales,
    labels=products,
    autopct="%1.1f%%",
    explode=(0, 0, 0, 0.1, 0),
    shadow=True,
    startangle=90
)
plt.title("Product Sales Contribution")
plt.axis("equal")
plt.show()
plt.figure(figsize=(7, 5))
plt.hist(profit, bins=5, color='green', edgecolor='black')
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()
plt.figure(figsize=(7, 5))
plt.scatter(sales, profit, color='purple')
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid()
plt.show()
print("\nSales and Profit Summary:")
print("Total Sales:", np.sum(sales))
print("Total Profit:", np.sum(profit))
print("Average Sales:", np.mean(sales))
print("Average Profit:", np.mean(profit))
print("Highest Sales:", np.max(sales))
print("Highest Profit:", np.max(profit))

print("\nProduct Sales and Profit Analysis Completed!")

