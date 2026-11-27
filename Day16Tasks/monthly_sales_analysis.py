# Monthly Sales Analysis sales = np.array([100, 150, 200, 180, 220, 300]) months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"].Create DataFrame Line graph → sales trend 
# Bar chart → month-wise comparison .Pie chart → contribution of each month .Histogram → frequency of sales values.Scatter plot → month index vs sales
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

print("Monthly Sales Data:")
print(df)
plt.figure(figsize=(7, 5))
plt.plot(months, sales, 'ro-', label="Sales")
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.grid()
plt.show()
plt.figure(figsize=(7, 5))
plt.bar(months, sales, color='blue')
plt.title("Month-wise Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
plt.figure(figsize=(6, 6))
plt.pie(
    sales,
    labels=months,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90
)
plt.title("Monthly Sales Contribution")
plt.axis("equal")
plt.show()
plt.figure(figsize=(7, 5))
plt.hist(sales, bins=5, color='green', edgecolor='black')
plt.title("Frequency of Sales Values")
plt.xlabel("Sales Values")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(7, 5))
plt.scatter(range(len(sales)), sales, color='purple')
plt.title("Month Index vs Sales")
plt.xlabel("Month Index")
plt.ylabel("Sales")
plt.show()
print("\nTotal Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Highest Sales:", np.max(sales))
print("Lowest Sales:", np.min(sales))

print("\nMonthly Sales Analysis Completed!")
