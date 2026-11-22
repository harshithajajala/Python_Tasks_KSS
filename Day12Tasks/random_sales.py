# Random Sales Simulation .A company wants to simulate 10 days of sales (range 100–500).Generate random integers using NumPy. 
# Print the array. 
# Find the average sales.

import numpy as np

sales = np.random.randint(100, 501, size=10)

print("Sales:", sales)
print("Average Sales:", np.mean(sales))
