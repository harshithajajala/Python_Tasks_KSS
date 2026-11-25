# Basic File Logger A system logs user actions.Take user input Store logs in a file .Use loop to allow multiple entries 
# Handle file errors using exception handling.

try:
    with open("user_logs.txt", "a") as file:

        while True:
            log = input("Enter your activity (exit to stop): ")

            if log.lower() == "exit":
                break

            file.write(log + "\n")

    print("Logs saved successfully")

except OSError:
    print("File error occurred")
