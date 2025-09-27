nums = [1, 2, 3, 4, 5]

squares = [x**2 for x in nums]  
even = [x for x in nums if x % 2 == 0]

print(squares)   # [1, 4, 9, 16, 25]
print(even)      # [2, 4]
