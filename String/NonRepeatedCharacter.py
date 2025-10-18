def first_non_repeated_char(str):
    count = {}
    for ch in str:
        count[ch] = count.get(ch,0) + 1

str = "aabbcde"
print(first_non_repeated_char(str))  
