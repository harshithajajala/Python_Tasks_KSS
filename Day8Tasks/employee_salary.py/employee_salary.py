# Employee Salary Management System

# Read employee details
file = open("employees.txt", "r")

employees = []

for line in file:
    name, salary = line.split()
    employees.append((name, int(salary)))

file.close()

# Display employee details
print("Employee Details:")

for name, salary in employees:
    print(name, salary)

# Find highest salary
highest = max(employees, key=lambda x: x[1])

print("\nHighest Salary Employee:")
print("Name:", highest[0])
print("Salary:", highest[1])

# Append new employee
file = open("employees.txt", "a")

name = input("\nEnter new employee name: ")
salary = input("Enter salary: ")

file.write("\n" + name + " " + salary)

file.close()

print("New employee added successfully!")