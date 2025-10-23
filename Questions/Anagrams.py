str1 = input("Enter the first string : ")
str2 = input("Enter the second string : ")

str1 = sorted(str1)
str2 = sorted(str2)

if str1 == str2:
    print("Strings are Anagrams.")
else:
    print("Strings are Not Anagrams.")
