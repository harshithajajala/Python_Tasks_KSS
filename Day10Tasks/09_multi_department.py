# Multi-Department Data Aggregation.A company collects employee counts from two branches. 
# Branch A: 
# [[10, 20], 
# [30, 40]] 
# Branch B: 
# [[5, 15], 
# [25, 35]] Combine the two matrices.Calculate the total employees across all departments.Print the combined matrix and total.

import numpy as np

branch_a = np.array([[10, 20],
                     [30, 40]])

branch_b = np.array([[5, 15],
                     [25, 35]])

combined = np.concatenate((branch_a, branch_b), axis=0)

total = np.sum(combined)

print("Combined Matrix:")
print(combined)

print("Total Employees:", total)
