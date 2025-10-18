# input : s = aaabccd
# output : a3b1c2d1

str = "aaabccd"
count = {}

for ch in str:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print(count)

result = "".join(f"{key}{value}" for key, value in count.items())
print(result)