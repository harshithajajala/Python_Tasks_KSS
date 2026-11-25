# Generator-based Log Reader.A large log file needs to be processed. Create a generator to read file line by line  Use loop to process logs 
# Use condition to filter errors .Count occurrences using a dictionary

def read_logs(filename):

    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


error_count = {}

try:
    for log in read_logs("logs.txt"):

        print(log)

        if "ERROR" in log:
            error_count[log] = error_count.get(log, 0) + 1

    print("\nError Count:")
    print(error_count)

except FileNotFoundError:
    print("Log file not found")
