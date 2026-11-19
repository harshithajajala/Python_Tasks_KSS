# Payment System.
# An online store supports multiple payment methods: CreditCard, UPI, and NetBanking. Create a base class Payment with a method process_payment() and override it in
# each payment type.


class Payment:
    def process_payment(self):
        print("Payment processing")


class CreditCard(Payment):
    def process_payment(self):
        print("Credit Card Payment")


class UPI(Payment):
    def process_payment(self):
        print("UPI Payment")


class NetBanking(Payment):
    def process_payment(self):
        print("Net Banking Payment")


c = CreditCard()
u = UPI()
n = NetBanking()
c.process_payment()
u.process_payment()
n.process_payment()
