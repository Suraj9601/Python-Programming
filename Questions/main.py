arr = [9,9,9]
num = ''.join(str(i) for i in arr)

num = int(num)
num += 1
num = str(num)
print(num)

result = []
for i in num:
    result.append(i)
print(result)