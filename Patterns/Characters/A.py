'''
      #       
    #   #
  #       #
# # # # # # #
#           #
#           #
#           #

'''

def pat():
    for i in range(1, 8):       
        for j in range(1, 8):      
            if (i == 4):                        
                print("#", end=" ")
            elif (i + j == 5) or (j - i == 3):    
                print("#", end=" ")
            elif (j == 1 and i > 4) or (j == 7 and i > 4): 
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()

pat()
