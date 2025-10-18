list = [1, 2, 3, 3, 2, 1]
count = {}
for i in list:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)
