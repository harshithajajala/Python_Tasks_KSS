# Combo of Numpy and Pandas Convert NumPy Array to Pandas Series A dataset: arr = np.array([10, 20, 30, 40]).
# Convert this NumPy array into a Pandas Series.
# Assign index labels: ["A", "B", "C", "D"].

arr = np.array([10, 20, 30, 40])

S = pd.Series(arr, index=["A", "B", "C", "D"])

print(S)
