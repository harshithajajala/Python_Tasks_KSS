
# Program to perform employee operations using a list of dictionaries

employees = [
    {"name": "John", "age": 25, "salary": 30000},
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 28, "salary": 40000},
    {"name": "David", "age": 35, "salary": 60000}
]

#  Find employee with highest salary
highest = max(employees, key=lambda x: x["salary"])

print("Highest salary employee:", highest["name"])

#  Filter employees with salary greater than 35000
print("Employees earning above 35000:")
for emp in employees:
    if emp["salary"] > 35000:
        print(emp["name"], emp["salary"])

#  Calculate average salary
total = 0
for emp in employees:
    total += emp["salary"]
average = total / len(employees)
print("Average salary:", average)

#  Create list containing employee names
names = []
for emp in employees:
    names.append(emp["name"])
print("Employee names:", names)
