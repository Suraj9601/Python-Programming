'''
# # # # # # # 
#
#
# # # # # # #
#
#
#

'''

def pat():
    for i in range(1, 8):         # rows
        for j in range(1, 8):     # cols
            if i == 1 or i == 4 or j == 1:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()

pat()
