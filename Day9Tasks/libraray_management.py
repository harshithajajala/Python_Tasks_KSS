# Library Management System.
# A library stores information about books and digital books. Create a base class Book with a constructor to initialize book details. Create a derived class EBook
# that adds file size information.


def even_numbers():
    num = 2

    while True:
        yield num
        num += 2


n = int(input("Enter N: "))

gen = even_numbers()

for i in range(n):
    print(next(gen))

