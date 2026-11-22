# Boolean Masking for Salary Analysis  
# Employee salaries:[25000, 40000, 15000, 50000, 30000],Filter salaries above 30000. 
# Count how many employees satisfy this condition.

import numpy as np

salary = np.array([25000, 40000, 15000, 50000, 30000])

result = salary[salary > 30000]

print("Salaries Above 30000:", result)
print("Number of Employees:", np.sum(salary > 30000))
