n = int(input("Enter number of terms: "))

a, b = 0, 1
print(f"Fibonacci Series:", "\n",a, "\n",b)

for i in range(2, n):
    c = a + b
    print(f"", c)
    a, b = b, c
