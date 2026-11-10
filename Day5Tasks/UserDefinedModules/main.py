

# Import calculator module
import calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition:", calculator.addition(a, b))

print("Subtraction:", calculator.subtraction(a, b))

print("Multiplication:", calculator.multiplication(a, b))

if b != 0:
    print("Division:", calculator.division(a, b))
else:
    print("Division is not possible")
