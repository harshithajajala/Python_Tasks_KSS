#  Create a dictionary containing student names and marks. Add a new student, update an existing student's marks and print all details.

# Program to add, update and display student details using a dictionary

students = {
    "Rahul": 85,
    "Amit": 90,
    "Priya": 78
}

# Adding a new student
students["Sneha"] = 95

# Updating existing student marks
students["Rahul"] = 88

# Displaying all student details
for name, marks in students.items():
    print(name, ":", marks)
