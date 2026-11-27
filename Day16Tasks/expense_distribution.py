# Expense Distribution Pie Chart.Monthly expenses: 
# expenses = np.array([500, 300, 200]) 
# labels = ["Food", "Rent", "Travel"] 
# Create a pie chart 
# Show percentage distribution


import numpy as np
import matplotlib.pyplot as plt

# Monthly expenses
expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]

# Create pie chart
plt.figure(figsize=(7, 7))

plt.pie(
    expenses,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90
)

# Add title
plt.title("Monthly Expense Distribution")

# Display chart
plt.show()
