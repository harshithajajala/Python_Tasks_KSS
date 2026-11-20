# Data Processing Pipeline.Convert the list into a NumPy array. Sort the array. Split the sorted array into two equal parts.  Calculate the sum of each part. 
# Output: 
# Sorted array 
# Two split arrays 
# Sum of each part

import numpy as np

data = [12, 7, 25, 3, 18, 10]

arr = np.array(data)

sorted_arr = np.sort(arr)

split_arr = np.split(sorted_arr, 2)

sum1 = np.sum(split_arr[0])
sum2 = np.sum(split_arr[1])

print("Sorted Array:", sorted_arr)

print("First Split:", split_arr[0])
print("Second Split:", split_arr[1])

print("Sum of First Part:", sum1)
print("Sum of Second Part:", sum2)
