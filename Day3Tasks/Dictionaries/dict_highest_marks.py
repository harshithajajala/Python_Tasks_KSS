#   Write a program to find the student with the highest marks from a dictionary. and give their file nmes


students = {
    "Rahul": 85,
    "Priya": 90,
    "Amit": 78
}
topper = max(students, key=students.get)
print("Topper:", topper)
print("Highest marks:", students[topper])
