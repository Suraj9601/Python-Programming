'''
#
#
#
#
#
#
# # # # # # #

'''

def pat():
    for i in range(1, 8):         # rows
        for j in range(1, 8):     # cols
            
            if j == 1 :
                print("#", end=" ")

            
            elif i == 7:
                print("#", end=" ")

            else:
                print(" ", end=" ")
        print()

pat()
