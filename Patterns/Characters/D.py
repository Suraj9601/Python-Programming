'''
# # # # # #   
#           #
#           #
#           #
#           #
#           #
# # # # # #

'''

def pat():
    for i in range(1, 8):         
        for j in range(1, 8):    
            
            if (i,j) in [(1,7),(7,7)]:   
                print(" ", end=" ")
                
            elif i == 1 or i == 7 or j == 1 or j == 7:
                print("#", end=" ")
                
            else:
                print(" ", end=" ")
        print()

pat()
