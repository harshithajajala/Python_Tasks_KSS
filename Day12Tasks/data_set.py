# A dataset contains: data = [[1, 2, 3], [4, 5], [6]] 
# Flatten the list using list comprehension.Then create a new list containing squares of only even numbers.

data = [[1, 2, 3], [4, 5], [6]]

flat = [num for row in data for num in row]

squares = [num ** 2 for num in flat if num % 2 == 0]

print("Flattened List:", flat)
print("Even Number Squares:", squares)
