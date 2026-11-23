# Student Marks Analysis .Given marks of 5 students in 3 subjects: marks = np.array([ 
# [70, 80, 90], 
# [60, 75, 85], 
# [50, 65, 70], 
# [90, 95, 85], 
# [40, 55, 60] ]). Calculate total marks of each student.Identify students whose total marks are above the class average.

import numpy as np

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [50, 65, 70],
    [90, 95, 85],
    [40, 55, 60]
])

total = np.sum(marks, axis=1)

avg = np.mean(total)

result = total[total > avg]

print("Total Marks:", total)
print("Class Average:", avg)
print("Above Average Students:", result)
