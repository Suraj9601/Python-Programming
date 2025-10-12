str = "banana apple mango"

words = str.split()  
word_list = []

for i in words:
    sorted_list = sorted(i)
    sorted_word = "".join(sorted_list)
    word_list.append(sorted_word)
   

final_str = " ".join(word_list)
print(final_str)