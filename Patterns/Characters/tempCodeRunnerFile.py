def pat():
    for i in range(1, 8):         # rows
        for j in range(1, 10):    # cols
            # Top curve
            if i == 1 and 3 <= j <= 7:
                print("#", end=" ")
            # Bottom curve
            elif i == 7 and 3 <= j <= 7:
                print("#", end=" ")
            # Upper left curve
            elif i == 2 and (j == 2 or j == 8):
                print("#", end=" ")
            # Lower left curve
            elif i == 6 and (j == 2 or j == 8):
                print("#", end=" ")
            # Left vertical
            elif 3 <= i <= 5 and j == 1:
                print("#", end=" ")
            # Right vertical
            elif 3 <= i <= 5 and j == 9:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()

pat()