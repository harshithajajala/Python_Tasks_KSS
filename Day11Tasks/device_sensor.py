# Device Sensor Value. An IoT device records a single sensor reading = 75.
# Create a 0-D NumPy array with this value. Print the value and check its number of dimensions.

import numpy as np

sensor = np.array(75)

print("Value:", sensor)
print("Dimensions:", sensor.ndim)

