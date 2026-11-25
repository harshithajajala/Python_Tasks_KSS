# Data Analysis Tool (NumPy + Pandas) Analyze student marks.Generate marks using NumPy .Convert into Pandas DataFrame Use conditions to filter passing students 
# Calculate mean using math/NumPy use loop to print results.

import numpy as np
import pandas as pd
marks = np.array([45, 67, 89, 56, 72])

names = ["Rahul", "Priya", "Amit", "Sneha", "Kiran"]

df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

print("Student Data:")
print(df)

passed = df[df["Marks"] >= 50]

print("\nPassing Students:")
print(passed)
average = np.mean(marks)

print("\nAverage Marks:", average)

for index, row in df.iterrows():
    print(row["Name"], row["Marks"])
