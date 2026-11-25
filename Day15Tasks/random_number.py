# Random Number Analyzer A system generates random numbers for testing.Use random to generate 10 numbers 
# Store in a list 
# Use loop + condition to count even/odd numbers 
# Use set to remove duplicates

import random

numbers = []
for i in range(10):
    num = random.randint(1, 50)
    numbers.append(num)

print("Random Numbers:", numbers)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

unique_numbers = set(numbers)

print("Even Numbers:", even)
print("Odd Numbers:", odd)
print("Unique Numbers:", unique_numbers)
