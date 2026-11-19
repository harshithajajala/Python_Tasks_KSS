#  Online Shopping System.
# An e-commerce company organizes products using multiple levels. Create classes Product → ElectronicProduct → MobilePhone using multilevel inheritance and display
# product details.


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand


class MobilePhone(ElectronicProduct):
    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Brand:", self.brand)


m = MobilePhone("Mobile", 20000, "Samsung")
m.display()
