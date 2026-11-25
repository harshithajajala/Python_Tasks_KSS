# Shopping Cart System A user adds items to a shopping cart.Store items in a list 
# Convert to set to remove duplicates 
# Use loop + condition to calculate total cost 
# Handle invalid input using try-excep

cart = []

prices = {
    "apple": 20,
    "banana": 10,
    "orange": 30,
    "mango": 40
}

try:
    n = int(input("How many items do you want? "))

    for i in range(n):
        item = input("Enter item name: ").lower()
        cart.append(item)

    unique_items = set(cart)

    total = 0

    for item in unique_items:
        if item in prices:
            total += prices[item]
            print(item, "=", prices[item])
        else:
            print(item, "is not available")

    print("Total Cost:", total)

except ValueError:
    print("Please enter a valid number")
