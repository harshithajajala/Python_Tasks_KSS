
# Program to count the frequency of each character in a string

text = "programming"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequency:", frequency)
