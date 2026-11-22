# Student Roll Numbers Extraction.A list contains roll numbers.[101, 102, 103, 104, 105, 106] 
# You want only the middle students (index 2 to 4).Use NumPy slicing to extract those values.

import numpy as np

roll_numbers = np.array([101, 102, 103, 104, 105, 106])

print(roll_numbers[2:5])
