#  Accessing Specific Data (Indexing) A Series contains: S = pd.Series([100, 200, 300, 400], index=["A", "B", "C", "D"]) 
#  Access values for B and D 
#  Return them as a subset

import pandas as pd
S = pd.Series(
    [100, 200, 300, 400],
    index=["A", "B", "C", "D"]
)
result = S.loc[["B", "D"]]

print(result)
