arr = [1, 2, 4, 3, 4, 3, 11, 7, 5, 2]
non_repeat = []

for i in arr:
    if i not in non_repeat:
        non_repeat.append(i)
print(non_repeat)
