#  Write a program to remove duplicate characters from a string. and also give file names

text = input("Enter a string: ")
result = ""
for ch in text:
    if ch not in result:
        result += ch
print("String after removing duplicates:", result)
