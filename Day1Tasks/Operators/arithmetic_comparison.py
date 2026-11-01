#  Combine arithmetic and comparison operators in one expression.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = (a + b) > (a * b)
print("Is sum greater than product?", result)
