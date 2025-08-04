'''
#           #     
# #         #
#   #       #
#     #     #
#       #   #
#         # #
#           #
'''


def pat():
    for i in range(1, 8):         # rows
        for j in range(1, 10):     # cols
            # if (i,j) in [(1,5),(2,4),(4,2),(3,3),(5,3),(6,4),(7,5)]:
            #     print("#", end=" ")
            
            if j == 1:
                print("#", end=" ")
                
            elif i == j:
                print("#", end=" ")
            elif j == 7:
                print("#", end=" ")
                
            else:
                print(" ", end=" ")
        print()

pat()