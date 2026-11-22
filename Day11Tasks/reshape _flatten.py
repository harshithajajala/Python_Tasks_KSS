#  Reshape and Flatten Image Data.An image is stored as a 2 × 3 matrix.[[1,2,3],[4,5,6]] 
#  Convert it into a NumPy array.Flatten the array into 1-D format. 
#  Print the flattened array.

import numpy as np

image = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flat_image = image.flatten()

print("Original Array:")
print(image)

print("Flattened Array:")
print(flat_image)
