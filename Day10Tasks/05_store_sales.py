#  Store Sales Comparison.Two stores record daily sales for 3 days. 
# Store A = [200, 250, 300] 
# Store B = [180, 270, 310].Store them in NumPy arrays.Find the daily difference in sales between the two stores.Print the resulting array.

import numpy as np

store_a = np.array([200, 250, 300])
store_b = np.array([180, 270, 310])

difference = store_a - store_b

print("Store A:", store_a)
print("Store B:", store_b)
print("Daily Difference:", difference)
