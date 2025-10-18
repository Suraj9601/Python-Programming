list = [1, 3, 2, 6, 4, 3, 2, 5]
Nonrepeat = []

for i in list:
    if list.count(i) == 1:
        Nonrepeat.append(i)


print(Nonrepeat)
