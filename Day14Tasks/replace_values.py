# Replace Values Using NumPy + Pandas A Series: S = pd.Series([10, 50, 30, 80, 20]) 
# Replace values greater than 40 with 0 using NumPy logic 
# Return updated Series

import numpy as np
import pandas as pd
S = pd.Series([10, 50, 30, 80, 20])
S[S > 40] = 0

print("Updated Series:")
print(S)
