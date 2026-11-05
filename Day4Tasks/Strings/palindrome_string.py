#  Write a program to check whether a string is a palindrome.

text = input("Enter a string: ")
if text == text[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
