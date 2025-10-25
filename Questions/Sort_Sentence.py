string = 'my name is suraj'
print(string)
words = string.split()


final = []
for word in words:
    sort_word = sorted(word)
    result = ''.join(sort_word)
    final.append(result)

output = ' '.join(final)
print(output)
