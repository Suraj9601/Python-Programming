def party_mode(num):
    mask = 0b101010 
    return num ^ mask

num = int(input("Enter 6-bit integer value: "))
new_state = party_mode(num)
print("New button state after Party Mode:", new_state)
