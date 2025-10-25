# input 50
# output 13

def checkads(num):
    b = bin(num)
    b=b[2:]
    print(b)
    bit_list = []
    for b in b:
        if b == '1':
            bit_list.append('0')
        else:
            bit_list.append('1')
    print(bit_list)
    final_bit = ''.join(bit_list)
    print(final_bit)
    interger = int(final_bit,2)
    print(interger)

num = int(input("Enter the number : "))
checkads(num)