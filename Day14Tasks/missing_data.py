# Missing Data Handling (NumPy + Pandas) .A dataset: arr = np.array([10, np.nan, 30, np.nan, 50]) 
# Convert to Pandas Series 
# Replace NaN values with the mean of the Series. 
# Print updated data.

import numpy as np
import pandas as pd
arr = np.array([10, np.nan, 30, np.nan, 50])
S = pd.Series(arr)
mean_value = S.mean()
S = S.fillna(mean_value)
print("Mean:", mean_value)
print("Updated Series:")
print(S)
