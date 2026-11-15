# Word Counter Program

file = open("article.txt", "r")

data = file.read()

words = len(data.split())
lines = len(data.splitlines())
characters = len(data)

print("Word Count:", words)
print("Line Count:", lines)
print("Character Count:", characters)

file.close()