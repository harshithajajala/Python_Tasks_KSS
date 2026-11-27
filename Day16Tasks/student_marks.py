# Student Marks Bar Chart.Marks of students: names = ["A", "B", "C", "D"] ,marks = np.array([70, 85, 60, 90]) 
# Create a DataFrame 
# Plot a bar graph 
# Show student names on X-axis


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Student names and marks
names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])

# Create DataFrame
df = pd.DataFrame({
    "Student": names,
    "Marks": marks
})

# Display DataFrame
print(df)

# Plot bar graph
plt.figure(figsize=(8, 5))
plt.bar(df["Student"], df["Marks"])

# Add labels and title
plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.title("Student Marks Bar Chart")

# Display graph
plt.show()


