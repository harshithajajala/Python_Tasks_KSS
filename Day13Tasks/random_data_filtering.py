# Random Data & Filtering .Generate random numbers: 
# nums = np.random.randint(1, 100, 10).
# Filter values that are divisible by 5. 
# Return sorted result.

import numpy as np

nums = np.random.randint(1, 100, 10)

result = nums[nums % 5 == 0]

sorted_result = np.sort(result)

print("Random Numbers:", nums)
print("Divisible by 5:", result)
print("Sorted Result:", sorted_result)
