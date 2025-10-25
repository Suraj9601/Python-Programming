string = input("Enter the string [B7U5P2] :")
print(f"Original String : {string}")

char = []
num = []

for ch in string:
    if ch.isalpha():
        char.append(ch)
    else:
        num.append(ch)

char = ''.join(sorted(char))
num = ''.join(sorted(num))
result = char + num

print(f"Sorted String : {result}")