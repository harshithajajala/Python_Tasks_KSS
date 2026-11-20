#  Temperature Monitoring System 
# A weather station records temperatures for two days. 
# Day 1: [30, 32, 31] 
# Day 2: [29, 33, 34] 
# Create a 2D NumPy array to store this data.
# Print the array.
# Find the total temperature recorded.

import numpy as np

day1 = [30, 32, 31]
day2 = [29, 33, 34]

arr = np.array([day1, day2])

print("Temperature Array:")
print(arr)

total = np.sum(arr)

print("Total Temperature:", total)
