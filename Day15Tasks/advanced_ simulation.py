# Advanced Simulation System.Simulate exam results and generate reports.Generate random marks using random Store in NumPy array.Convert to Pandas DataFrame.
# Use OOP to represent Student Use conditions + loops to assign grades Save report to file Handle errors using try-except .Use math module for statistics.

import random
import numpy as np
import pandas as pd
import math


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 75:
            return "B"

        elif self.marks >= 50:
            return "C"

        else:
            return "Fail"


try:
    names = ["Rahul", "Priya", "Amit", "Sneha", "Kiran"]

    marks = np.array([
        random.randint(0, 100) for i in range(5)
    ])

    students = []

    for i in range(len(names)):

        student = Student(names[i], int(marks[i]))
        students.append(student)

    data = []

    for student in students:

        data.append({
            "Name": student.name,
            "Marks": student.marks,
            "Grade": student.grade()
        })

    df = pd.DataFrame(data)

    print("Exam Results:")
    print(df)

    average = math.ceil(np.mean(marks))

    print("\nAverage Marks:", average)

    with open("exam_report.txt", "w") as file:
        file.write(df.to_string())
        file.write(f"\nAverage Marks: {average}")

    print("\nReport saved successfully")

except (ValueError, OSError) as e:
    print("Error:", e)
