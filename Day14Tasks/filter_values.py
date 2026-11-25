# Filter Values Using Condition.A dataset: arr = np.array([10, 25, 30, 15, 40]).
# Convert to Pandas Series 
# Filter values greater than 20

import numpy as np
import pandas as pd
arr = np.array([10, 25, 30, 15, 40])
S = pd.Series(arr)
result = S[S > 20]
print(result)
