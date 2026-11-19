#  Bank Account System (Class, Object, Constructor) 
#  A bank wants to manage customer accounts. Create a BankAccount class with a constructor to initialize account number and balance. Implement methods to deposit,
#  withdraw, and display balance.

class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display(self):
        print("Account Number:", self.acc_no)
        print("Balance:", self.balance)


b1 = BankAccount(12345, 5000)
b1.deposit(2000)
b1.withdraw(1000)
b1.display()
