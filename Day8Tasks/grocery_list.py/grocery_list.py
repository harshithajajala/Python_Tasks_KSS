# Grocery List Manager

file = open("grocery.txt", "w")

n = int(input("Enter number of items: "))

for i in range(n):
    item = input("Enter grocery item: ")
    file.write(item + "\n")

file.close()

print("Grocery items saved successfully!")