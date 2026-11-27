# Pie Chart with Conditional Data scores = np.array([40, 60, 80, 30, 90]) . Categorize into: Pass (>50) 
# Fail (<=50) 
# Count using NumPy/Pandas 
# Plot pie chart for Pass vs Fail 


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Student scores
scores = np.array([40, 60, 80, 30, 90])

# Categorize scores
pass_count = np.sum(scores > 50)
fail_count = np.sum(scores <= 50)

# Create DataFrame
df = pd.DataFrame({
    "Category": ["Pass", "Fail"],
    "Count": [pass_count, fail_count]
})

print(df)

# Plot pie chart
plt.figure(figsize=(6, 6))

plt.pie(
    df["Count"],
    labels=df["Category"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Pass vs Fail Distribution")
plt.show()
