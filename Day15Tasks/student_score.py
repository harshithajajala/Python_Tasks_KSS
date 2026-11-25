# Student Score Processor A teacher stores student names and marks in a list of tuples. Convert data into a dictionary Use a loop + condition to find students scoring
# above 50. 
# Use math module to calculate average. 
# Store results in a text file.

import math

students = [
    ("Rahul", 75),
    ("Priya", 45),
    ("Amit", 85),
    ("Sneha", 60),
    ("Kiran", 35)
]


student_dict = dict(students)

print("Student Marks:", student_dict)

total = 0
count = 0

with open("student_results.txt", "w") as file:
    file.write("Students scoring above 50:\n")

    for name, marks in student_dict.items():
        if marks > 50:
            print(name, marks)
            file.write(f"{name}: {marks}\n")

        total += marks
        count += 1

average = math.ceil(total / count)

print("Average Marks:", average)
