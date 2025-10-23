string = input("Enter the string : ")
count = {}

for ch in string:
    if ch not in count:
        count[ch] = 1
    else:
        count[ch] += 1

print(count)