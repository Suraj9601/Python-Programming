'''
      # # # # 
    #
    #
    #
      # # # #
'''

def pat():
    n = 5
    for i in range(1, n+1):          # rows
        for j in range(1, n+1):      # cols
            if (i == 1 and j > 1) or (i == n and j > 1) or (j == 1 and i != 1 and i != n):
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()

pat()
