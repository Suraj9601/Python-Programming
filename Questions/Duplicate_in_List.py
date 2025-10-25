arr = [3,2,5,2,5,9,7,4,6,9]
real_arr = []
duplicate = []

for i in arr:
    if i not in real_arr:
        real_arr.append(i)
    else:
        duplicate.append(i)
print(duplicate)
