# Notes Reader Program

file = open("notes.txt", "r")

data = file.read()

print("Student Notes:")
print(data)

file.close()