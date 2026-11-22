# Even Number Filter. A system stores numbers: 
# nums = [1, 2, 3, 4, 5, 6] .Use list comprehension to create a new list containing only even numbers.

nums = [1, 2, 3, 4, 5, 6]

even = [i for i in nums if i % 2 == 0]

print("Even Numbers:", even)
