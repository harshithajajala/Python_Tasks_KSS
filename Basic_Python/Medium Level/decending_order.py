
# Program to sort student marks in descending order and display top two students

students = {
    "Rahul": 85,
    "Amit": 92,
    "Priya": 78,
    "Sneha": 95
}

sorted_students = sorted(
    students.items(),
    key=lambda x: x[1],
    reverse=True
)

print("Students sorted by marks:")

for name, marks in sorted_students:
    print(name, ":", marks)

print("Top two students:")

for name, marks in sorted_students[:2]:
    print(name, ":", marks)
