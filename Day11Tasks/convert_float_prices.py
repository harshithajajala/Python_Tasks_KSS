# Convert Float Prices to Integer.A shop stores product prices.[10.5, 20.8, 15.3] 
# The billing system requires integer values.  
# Convert the array from float to integer using as type().

import numpy as np

prices = np.array([10.5, 20.8, 15.3])

integer_prices = prices.astype(int)

print("Original:", prices)
print("Converted:", integer_prices)
