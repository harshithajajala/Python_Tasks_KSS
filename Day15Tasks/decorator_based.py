# Decorator-based Access Control.Restrict access to certain functions. Create a decorator to check user role.Use condition inside decorator . Apply decorator
# to multiple functions . Store roles in a dictionary.

roles = {
    "Rahul": "admin",
    "Priya": "user"
}

current_user = "Rahul"


def check_role(func):

    def wrapper():

        if roles.get(current_user) == "admin":
            return func()
        else:
            print("Access Denied")

    return wrapper


@check_role
def delete_data():
    print("Data deleted successfully")


@check_role
def view_data():
    print("Viewing data")


delete_data()
view_data()
