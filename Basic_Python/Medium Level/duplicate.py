
# Program to remove duplicate elements from a list without using set()

numbers = [1, 2, 3, 2, 4, 1, 5, 3]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("List without duplicates:", unique)
