num = int(input("Enter the number :"))

if num <= 1:
    print("Not Prime.")
elif num == 2:
    print("Prime.")
elif num % 2 == 0:
    print("Not Prime.")
else:
    for i in range(3,int(num**0.5 + 1), 2):
        if num % i == 0:
            print("Not Prime.")