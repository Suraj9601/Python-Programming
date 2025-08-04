'''
#               # 
# #           # #
#   #       #   #
#     #   #     #
#       #       #
#               #
#               #
#               #

'''


def pat():
    print()
    for i in range(1, 10):         
        for j in range(1, 10):   
            
            if j == 1 and i<9:
                print("#", end=" ")
            
            elif (i,j) in [(4,6),(3,7),(2,8)]:
                print("#", end=" ")
                
            elif i == j and j <= 5:
                print("#", end=" ")
            
                
            elif j == 9 and i<9:
                print("#", end=" ")
                
            else:
                print(" ", end=" ")
        print()

pat()