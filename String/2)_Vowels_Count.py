string = "surauj"  # a,e,u,i,o
count = {}
vowels = "aeiou"
for ch in string:
    if ch in vowels:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
        
print(count)
