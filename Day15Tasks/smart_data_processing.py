# Smart Data Processing Pipeline .A system processes numeric data from file. Read numbers from a file .Use NumPy for calculations (mean, std).Convert results to
# pandas DataFrame.Use exception handling for bad data.Use a generator to stream data . Apply decorator to measure execution time.

import numpy as np
import pandas as pd
import time


# Decorator to calculate execution time
def calculate_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution Time:", end - start)

        return result

    return wrapper


# Generator
def read_numbers(filename):

    with open(filename, "r") as file:
        for line in file:
            for value in line.split():
                yield float(value)


@calculate_time
def process_data():

    try:
        numbers = list(read_numbers("numbers.txt"))

        arr = np.array(numbers)

        mean = np.mean(arr)
        std = np.std(arr)

        df = pd.DataFrame({
            "Mean": [mean],
            "Standard Deviation": [std]
        })

        print(df)

    except (ValueError, OSError) as e:
        print("Error:", e)


process_data()





