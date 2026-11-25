# Missing City Data (NaN Handling) A dataset contains city populations: cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000} 
# You want data for: ["Delhi", "Chennai", "Bangalore"] 
# Create a Series with the above index 
# Identify which cities have missing values (NaN)

import pandas as pd

cities = {
    "Delhi": 2000000,
    "Mumbai": 3000000,
    "Chennai": 1500000
}

S = pd.Series(cities, index=["Delhi", "Chennai", "Bangalore"])

print("City Population:")
print(S)
print("\nMissing Values:")
print(S.isna())
