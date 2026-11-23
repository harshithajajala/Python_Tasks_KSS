# Temperature Alert System Temperatures recorded in a city: temps = np.array([28, 32, 35, 31, 29, 40, 38]) 
# Identify days where temperature is greater than 30. 
# Return their indices.

import numpy as np

temps = np.array([28, 32, 35, 31, 29, 40, 38])

indexes = np.where(temps > 30)

print("Temperatures Above 30:", temps[temps > 30])
print("Day Indexes:", indexes[0])
