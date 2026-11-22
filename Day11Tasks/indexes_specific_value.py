# Find Indexes of Specific Value.A quality check system stores product defect codes.[2, 4, 1, 4, 3, 4, 5].Find the indexes where value = 4 using NumPy searching.

import numpy as np

scores = np.array([50, 60, 70, 80, 90, 100, 110, 120])

parts = np.array_split(scores, 4)

for part in parts:
    print(part)
