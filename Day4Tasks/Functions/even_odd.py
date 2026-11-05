#   Write a function to check whether a number is even or odd.

def even_odd(n):
    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
num = int(input("Enter a number: "))
even_odd(num)
