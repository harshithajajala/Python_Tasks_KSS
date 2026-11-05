#  Write a function to find the sum of elements in a list using a user-defined function. def list_sum(numbers):

def list_sum(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total

numbers = [10, 20, 30, 40]
print("Sum of list:", list_sum(numbers))
