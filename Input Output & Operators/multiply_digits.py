# 56. Multiply all digits of a number.

num = int(input("Enter a number: "))
product = 1

while num > 0:
    digit = num % 10
    product *= digit
    num = num // 10

print("Multiplication of all digits:", product)
