'''
#           # 
#           #
#           #
# # # # # # #
#           #
#           #
#           #

'''

def pat():
    for i in range(1, 8):         # rows
        for j in range(1, 8):     # cols
            
            if i == 4 :
                print("*", end=" ")

            
            elif j == 1:
                print("*", end=" ")

            elif j == 7:
                print("*", end=" ")

            else:
                print(" ", end=" ")
        print()

pat()
