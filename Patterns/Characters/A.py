'''
# # # # # # # 
#           #
#           #
# # # # # # #
#           #
#           #
#           # 

'''

def pat():
    for i in range(1,8): # row
        for j in range(1,8): # column
            if i == 1 or j == 1 or i == 4 or j == 7:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()
    return

pat()