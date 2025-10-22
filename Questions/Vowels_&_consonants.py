string = input("Enter the string : ").lower()
vowels = 'aeiou'
count = {}
vowel = {}
consonants = {}

for ch in string:
    if ch not in count:
        count[ch] = 1
    else : 
        count[ch] += 1


for k,v in count.items():
    if k in vowels:
        vowel[k] = v
    else:
        consonants[k] = v

print("Vowels = ",vowel)
print("Consonants", consonants)