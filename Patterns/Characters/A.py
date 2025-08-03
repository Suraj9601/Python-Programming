def pat():
    for i in range(1,6): # row
        for j in range(1,6): # column
            if i == 1 or j == 1 or i == 3 or j == 5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    return

pat()