# Write a program to check whether a given number is a Strong number.

num = int(input("Enter a number: "))
temp = num
total = 0
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    total = total + fact
    temp = temp // 10

if total == num:
    print(num, "is a Strong number")
else:
    print(num, "is not a Strong number")

