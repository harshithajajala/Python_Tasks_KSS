#   Write a Python program that generates 20 random numbers between 1 and 200 using the random module and store them in a list. 
#   Then using the math module, compute and display: 
#   Maximum value 
#   Minimum value 
#   Square root of the maximum number 
#   Logarithm of the minimum number


import random
import math
numbers = []
for i in range(20):
    num = random.randint(1, 200)
    numbers.append(num)
print("Random numbers:", numbers)
maximum = max(numbers)
minimum = min(numbers)
print("Maximum value:", maximum)
print("Minimum value:", minimum)
print("Square root of maximum:", math.sqrt(maximum))
print("Logarithm of minimum:", math.log(minimum))
