sentence = input("Enter the Sentence : ")
words = sentence.split()
words.reverse()

result = ' '.join(words)
print(result)