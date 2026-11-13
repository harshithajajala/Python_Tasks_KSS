# Student Marks Management System

# 1. Tuple - Store subject names
subjects = ("Math", "Science", "English")

# 2. Set - Store unique student names
student_names = set()

# 3. Dictionary - Store student names and marks
students = {}

# 4. Function to add a student
def add_student():
    name = input("Enter student name: ").strip()
    if name == "":
        print("Student name cannot be empty.")
        return

    if name in student_names:
        print("Student already exists!")
        return

    marks = []

    try:
        for subject in subjects:
            mark = float(input(f"Enter marks for {subject}: "))
            marks.append(mark)

        students[name] = marks
        student_names.add(name)

        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Please enter numeric marks.")

    except TypeError:
        print("Marks data type error.")


# 5. Function to display all student records
def display_students():

    if not students:
        print("No student records available.")
        return

    for name, marks in students.items():
        print(name, ":", marks)


# 6. Recursive function to calculate total marks
def calculate_total(marks):

    if not isinstance(marks, list):
        raise TypeError("Marks must be a list.")

    if len(marks) == 0:
        return 0

    if not isinstance(marks[0], (int, float)):
        raise TypeError("Marks must be numeric.")

    return marks[0] + calculate_total(marks[1:])


# 7. Function to calculate average marks
def calculate_average():

    name = input(
        "Enter student name to calculate average: "
    ).strip()

    try:
        if name not in students:
            raise NameError("Student name not found.")

        marks = students[name]

        total = calculate_total(marks)

        average = total / len(marks)

        print("Total Marks:", total)
        print("Average Marks:", average)

    except NameError:
        print("Student name not found.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except TypeError:
        print("Marks data type error.")


# 8. Main menu
while True:

    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            display_students()

        elif choice == 3:
            calculate_average()

        elif choice == 4:
            print("Thank you! Program exited.")
            break

        else:
            print("Invalid choice! Select 1 to 4.")

    except ValueError:
        print("Please enter a valid numeric choice.")