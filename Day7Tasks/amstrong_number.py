#  Write a program to check whether a given number is an Armstrong number or not.

num = int(input("Enter a number: "))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** 3
    temp = temp // 10

if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
