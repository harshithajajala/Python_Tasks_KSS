# Sorting Product Prices 
# An e-commerce company stores product prices in a NumPy array. 
# Prices = [499, 299, 799, 199, 599]  
# Convert it into a NumPy array. 
# Sort the prices in ascending order.

import numpy as np

prices = [499, 299, 799, 199, 599]

arr = np.array(prices)

sorted_prices = np.sort(arr)

print("Original Prices:", arr)
print("Sorted Prices:", sorted_prices)
