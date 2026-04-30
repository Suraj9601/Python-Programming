fib = [0, 1]     # Initial two Fibonacci numbers

n = 5            # How many additional terms you want

for i in range(n):
    fib.append(fib[-1] + fib[-2])   # Add last two numbers

# Print Fibonacci list as comma-separated values
print(', '.join(str(e) for e in fib))
