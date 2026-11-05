#   Write a program to check whether a substring exists in a string.

text = input("Enter a string: ")
sub = input("Enter a substring: ")
if sub in text:
    print("Substring exists")
else:
    print("Substring does not exist")
