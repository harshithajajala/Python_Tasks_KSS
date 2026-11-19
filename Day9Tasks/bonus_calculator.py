# Employee Bonus Calculator.
# A company wants to apply a bonus calculation automatically before displaying the salary. Create an Employee class and use a decorator that modifies the salary by 
# adding a bonus before displaying it.


def bonus_calculator(func):
    def wrapper(self):
        self.salary = self.salary + self.bonus
        func(self)
    return wrapper


class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    @bonus_calculator
    def display_salary(self):
        print("Employee Name:", self.name)
        print("Final Salary:", self.salary)


e1 = Employee("Harshitha", 30000, 5000)
e1.display_salary()
