# Small Shop Customer Purchase Management System

# 1. Dictionary - Store product names and details
# Tuple - Store price and category of each product

products = {
    "Pen": (10, "Stationery"),
    "Notebook": (50, "Stationery"),
    "Pencil": (5, "Stationery"),
    "Eraser": (5, "Stationery")
}

# 2. Set - Store unique product categories
categories = {"Stationery"}

# 3. List - Store items added to cart
cart = []


# 4. Function to display products
def display_products():

    print("\nAvailable Products:")

    for name, details in products.items():
        price, category = details
        print(name, ":", price, "| Category:", category)

    print("\nProduct Categories:", categories)


# 5. Function to add items to cart
def add_to_cart():

    product_name = input("Enter product name: ").strip().title()

    try:
        if product_name not in products:
            raise NameError("Product not found in store.")

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        price, category = products[product_name]

        # Store product details as a tuple in the list
        cart.append((product_name, quantity, price))

        print("Item added to cart successfully.")

    except ValueError:
        print("Invalid quantity! Please enter a number.")

    except NameError:
        print("Product not found in store.")

    except TypeError:
        print("Cart data type error.")


# 6. Recursive function to calculate total bill
def calculate_total(items):

    if not isinstance(items, list):
        raise TypeError("Cart must be a list.")

    # Base condition
    if len(items) == 0:
        return 0

    item = items[0]

    if not isinstance(item, tuple) or len(item) != 3:
        raise TypeError("Invalid cart data.")

    name, quantity, price = item

    if not isinstance(quantity, (int, float)):
        raise TypeError("Invalid quantity data.")

    if not isinstance(price, (int, float)):
        raise TypeError("Invalid price data.")

    # Recursive calculation
    return (quantity * price) + calculate_total(items[1:])


# 7. Function to view total bill
def view_total_bill():

    try:
        if len(cart) == 0:
            raise ZeroDivisionError("Cart is empty.")

        print("\nItems in Cart:")

        for name, quantity, price in cart:
            print(name, "x", quantity)

        total = calculate_total(cart)

        print("\nTotal Bill:", total)

    except ZeroDivisionError:
        print("Calculation error: division by zero.")

    except TypeError:
        print("Cart data type error.")


# 8. Main menu
while True:

    print("\n1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            display_products()

        elif choice == 2:
            add_to_cart()

        elif choice == 3:
            view_total_bill()

        elif choice == 4:
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice! Select 1 to 4.")

    except ValueError:
        print("Please enter a valid numeric choice.")