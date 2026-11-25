# Student Marks DataFrame Analysis .A DataFrame: data = pd.DataFrame({ "Name": ["A", "B", "C"], 
# "Math": [80, 70, 60], 
# "Science": [90, 60, 70] }) 
#  Add a new column Total = Math + Science 
#  Find the student with the highest total marks

import pandas as pd
data = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Math": [80, 70, 60],
    "Science": [90, 60, 70]
})

data["Total"] = data["Math"] + data["Science"]

print("Student Marks:")
print(data)

index = data["Total"].idxmax()

print("\nHighest Scoring Student:")
print(data.loc[index, "Name"])

print("Highest Total:", data["Total"].max())
