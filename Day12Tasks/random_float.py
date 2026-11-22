# Random Dataset Normalization + Filtering 
# Generate 8 random float values between 0 and 1.Normalize by multiplying with 100 
# Filter values greater than 50 
# Sort the filtered values

import numpy as np

arr = np.random.rand(8)

normalized = arr * 100

filtered = normalized[normalized > 50]

sorted_values = np.sort(filtered)

print("Original Values:", arr)
print("Normalized Values:", normalized)
print("Filtered Values:", filtered)
print("Sorted Values:", sorted_values)
