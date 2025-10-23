string = input("Enter the string : ").lower()
new_str = ""

for ch in string:
    if ch not in new_str:
        new_str += ch
print(new_str)