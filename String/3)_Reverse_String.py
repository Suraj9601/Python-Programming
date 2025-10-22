str = input("Enter String : ")

# Using Built-in Function
str1 = "".join(reversed(str))
print(str1)

# Without Using built in Function
reverse_str = str[::-1]
print(reverse_str)
