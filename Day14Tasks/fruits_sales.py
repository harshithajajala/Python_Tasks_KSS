# Fruit Sales Comparison (Series Addition) A shop tracks fruit sales: 
# S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"]) 
# S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"])  
# Add both series 
# Find the total sales of all fruits combined

import pandas as pd

S1 = pd.Series([10, 20, 30],
               index=["apple", "banana", "cherry"])

S2 = pd.Series([5, 15, 25],
               index=["apple", "banana", "cherry"])

result = S1 + S2
print("Fruit-wise Sales:")
print(result)
total = result.sum()

print("Total Sales:", total)
