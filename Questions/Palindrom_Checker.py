string = input("Enter the String : ")
string = string.lower()

reverse_str = string[::-1]

if string == reverse_str:
    print("Enetred String is Palindrom.")
else:
    print("Entered String is not Palindrom.")