#  Given a tuple (10, 20, 30, 40, 50), print the first, last and middle elements.


numbers = (10, 20, 30, 40, 50)

first = numbers[0]
last = numbers[-1]
middle = numbers[len(numbers) // 2]

print("First element:", first)
print("Last element:", last)
print("Middle element:", middle)
