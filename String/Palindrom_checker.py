str = "Mam"
str = str.lower()
str_reverse = str[::-1]
print(str_reverse)

if str == str_reverse:
    print(f"String is Palindrom.")
else:
    print("String is Not Palindrom.")
