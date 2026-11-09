#  Reverse a string without using built-in reverse functions.

text = input("Enter a string: ")
reverse = ""
for char in text:
    reverse = char + reverse

print("Original string:", text)
print("Reversed string:", reverse)
