def character_count(str):
    print(f"Character Count from string : '{str}'")
    char_count = {}

    for ch in str:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1
    return char_count


str = "banana"
result = character_count(str)
print(result)
