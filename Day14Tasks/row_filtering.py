# Row Filtering + Aggregation .A dataset: arr = np.array([[100, 200], [150, 250], [80, 120], [300, 400] ]) .Convert to DataFrame with columns "Sales", "Profit" 
# Filter rows where Sales > 100 
# Find average Profit of filtered rows

import numpy as np
import pandas as pd

arr = np.array([
    [100, 200],
    [150, 250],
    [80, 120],
    [300, 400]
])

df = pd.DataFrame(arr, columns=["Sales", "Profit"])

result = df[df["Sales"] > 100]

print("Filtered Data:")
print(result)

average = result["Profit"].mean()

print("Average Profit:", average)
