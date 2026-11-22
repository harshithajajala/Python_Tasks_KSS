# Random Matrix and Condition Filtering.Generate a 3×3 matrix of random numbers (0–50). 
# Filter elements greater than 25. 
# Print filtered values.

import numpy as np

matrix = np.random.randint(0, 51, size=(3, 3))

print("Original Matrix:")
print(matrix)

result = matrix[matrix > 25]

print("Values Greater Than 25:", result)
