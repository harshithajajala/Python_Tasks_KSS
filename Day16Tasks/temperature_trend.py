# Temperature Trend Line Plot Daily temperatures: 
# temps = np.array([28, 30, 32, 31, 29])  
# Convert into Pandas Series 
# Plot a line graph 
# Add title and grid


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Daily temperature data
temps = np.array([28, 30, 32, 31, 29])

# Convert NumPy array into Pandas Series
temperature = pd.Series(temps)

# Display temperature Series
print(temperature)

# Plot line graph
plt.figure(figsize=(8, 5))
plt.plot(temperature, marker='o')

# Add title and labels
plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")

# Add grid
plt.grid(True)

# Display graph
plt.show()
