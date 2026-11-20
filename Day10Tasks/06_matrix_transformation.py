#  Matrix Transformation in Image Processing.
# [[1, 2], [3, 4]] 
# Create a NumPy array for this matrix.Find its transpose.Print both matrices.

import numpy as np

matrix = np.array([[1, 2],
                   [3, 4]])

transpose = matrix.T

print("Original Matrix:")
print(matrix)

print("Transpose Matrix:")
print(transpose)
