# Import functions from both modules

from utilities.math_operations import add, multiply
from utilities.string_operations import convert_uppercase, count_characters


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


print("Addition:", add(a, b))
print("Multiplication:", multiply(a, b))


text = input("Enter a string: ")


print("Uppercase:", 
convert_uppercase(text))
print("Character count:",
count_characters(text))