# Employee Salary Insights salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000]) departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"] 
# Convert into DataFrame Plot:Line graph → salary trend.Bar chart → department-wise salary comparison .Pie chart → department distribution 
# Histogram → salary distribution.Scatter plot → index vs salary.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
df = pd.DataFrame({
    "Department": departments,
    "Salary": salaries
})

print("Employee Salary Details:")
print(df)

plt.figure(figsize=(7, 5))
plt.plot(range(len(salaries)), salaries, 'ro-', label="Salary")
plt.title("Employee Salary Trend")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.legend()
plt.grid()
plt.show()

department_salary = df.groupby("Department")["Salary"].mean()

plt.figure(figsize=(7, 5))
plt.bar(department_salary.index, department_salary.values, color='blue')
plt.title("Department-wise Average Salary")
plt.xlabel("Departments")
plt.ylabel("Average Salary")
plt.show()

department_count = df["Department"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    department_count.values,
    labels=department_count.index,
    autopct="%1.1f%%",
    explode=[0.1, 0, 0],
    shadow=True,
    startangle=90
)
plt.title("Department Distribution")
plt.axis("equal")
plt.show()
plt.figure(figsize=(7, 5))
plt.hist(salaries, bins=5, color='green', edgecolor='black')
plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()
plt.figure(figsize=(7, 5))
plt.scatter(range(len(salaries)), salaries, color='purple')
plt.title("Employee Index vs Salary")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.show()

print("\nSalary Summary:")
print("Total Salary:", np.sum(salaries))
print("Average Salary:", np.mean(salaries))
print("Highest Salary:", np.max(salaries))
print("Lowest Salary:", np.min(salaries))

print("\nEmployee Salary Analysis Completed!")
