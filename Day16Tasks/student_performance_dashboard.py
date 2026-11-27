# Student Performance Dashboard .A school records marks of students in one subject:marks = np.array([45, 67, 89, 56, 72, 91, 38]).
# students = ["A", "B", "C", "D", "E", "F", "G"].Convert to Pandas DataFrame.Plot:Line graph → trend of marks .Bar chart → student vs marks.
# Pie chart → Pass (>50) vs Fail .Histogram → distribution of marks .Scatter plot → index vs marks.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

print("Student Performance Data:")
print(df)

df["Result"] = np.where(df["Marks"] > 50, "Pass", "Fail")

plt.figure(figsize=(7, 5))
plt.plot(students, marks, 'ro-', label="Marks")
plt.title("Student Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.grid()
plt.show()
plt.figure(figsize=(7, 5))
plt.bar(students, marks, color='blue')
plt.title("Student vs Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

pass_count = sum(df["Result"] == "Pass")
fail_count = sum(df["Result"] == "Fail")

plt.figure(figsize=(6, 6))
plt.pie(
    [pass_count, fail_count],
    labels=["Pass", "Fail"],
    autopct="%1.1f%%",
    explode=(0.1, 0),
    shadow=True,
    startangle=90
)
plt.title("Pass vs Fail")
plt.axis("equal")
plt.show()

plt.figure(figsize=(7, 5))
plt.hist(marks, bins=5, color='green', edgecolor='black')
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
plt.figure(figsize=(7, 5))
plt.scatter(range(len(marks)), marks, color='purple')
plt.title("Index vs Marks")
plt.xlabel("Student Index")
plt.ylabel("Marks")
plt.show()

print("\nDashboard Created Successfully!")
