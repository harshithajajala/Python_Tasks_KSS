#  Write a program to find the second largest number in a list. and also give me file names

numbers = [10, 50, 30, 80, 60]
unique_numbers = list(set(numbers))
unique_numbers.sort()
print("Second largest number:", unique_numbers[-2])
