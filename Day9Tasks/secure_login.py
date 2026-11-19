# Secure Login System.
# A web application wants to ensure that users are authenticated before accessing sensitive functions. Create a decorator that checks whether the user is logged in
# before allowing access to a function.


def login_required(func):
    def wrapper():
        logged_in = True

        if logged_in:
            print("Login successful!")
            func()
        else:
            print("Please login first")

    return wrapper


@login_required
def dashboard():
    print("Welcome to Dashboard")
dashboard()
