arr = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

for sub in arr:
    print(sub)

for sub in arr:
    sum = 0
    for i in sub:
        sum += i
    print(f"Sum of {sub} : {sum}")