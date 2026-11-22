# Replace Values Using Filtering .A dataset contains: [5, 12, 18, 7, 25, 30]. Replace all values greater than 15 with 0 using NumPy filtering.

import numpy as np

arr = np.array([5, 12, 18, 7, 25, 30])

arr[arr > 15] = 0

print("Updated Array:", arr)

