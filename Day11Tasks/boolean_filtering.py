# Filter High Temperature Values.A weather station records temperatures.[28, 31, 35, 27, 40, 22].The system needs temperatures above 30°C. Filter the values greater
# than 30 using NumPy boolean filtering.

import numpy as np

temperature = np.array([28, 31, 35, 27, 40, 22])

result = temperature[temperature > 30]

print("Temperatures above 30:", result)
