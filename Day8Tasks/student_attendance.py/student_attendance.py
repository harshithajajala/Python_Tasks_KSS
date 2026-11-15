# Student Attendance Record 

name = input("Enter student name: ")

with open("attendance.txt", "a") as file:
    file.write(name + "\n")

with open("attendance.txt", "r") as file:
    print("\nStudent Attendance Records:")
    print(file.read())



