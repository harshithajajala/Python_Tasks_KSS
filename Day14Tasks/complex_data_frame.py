# Complex DataFrame Transformation .A DataFrame: df = pd.DataFrame({ "Name": ["A", "B", "C", "D"], "Marks": [50, 80, 30, 90] })  
# Students scoring below 50 failed  
# Create a column Status ("Pass"/"Fail") 
# Filter only passed students 
# Calculate average marks of passed students

import numpy as np
import pandas as pd
df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [50, 80, 30, 90]
})

df["Status"] = np.where(df["Marks"] < 50, "Fail", "Pass")

passed = df[df["Status"] == "Pass"]

print("Student Results:")
print(df)

print("\nPassed Students:")
print(passed)

average = passed["Marks"].mean()

print("\nAverage Marks of Passed Students:", average)
