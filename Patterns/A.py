# Print 'A' Pattern in Python

n = 7   # height of A

for i in range(n):
    for j in range(n):
        # Top line, middle line, left & right slants
        if ((j == 0 or j == n-1) and i != 0) or (i == 0 and j > 0 and j < n-1) or (i == n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
