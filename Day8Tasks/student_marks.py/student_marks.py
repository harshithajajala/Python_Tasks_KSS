# Student Marks File Analyzer

file = open("marks.txt", "r")

total = 0
count = 0

print("Student Records:")

for line in file:
    name, marks = line.split()
    marks = int(marks)

    print(name, marks)

    total = total + marks
    count = count + 1

file.close()

average = total / count

print("Average Marks:", average)