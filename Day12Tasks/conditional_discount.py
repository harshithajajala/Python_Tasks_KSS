# Conditional Discount System. A shop has prices = [100, 200, 300, 400] 
# Apply a 10% discount only if price > 200. 
# Use list comprehension with condition to create updated price list.

prices = [100, 200, 300, 400]

updated = [p * 0.9 if p > 200 else p for p in prices]

print("Updated Prices:", updated)
