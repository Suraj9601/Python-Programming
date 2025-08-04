'''
      #    
  #       #
#           #
#           #
#           #
  #       #  
      #   

'''

def pat():
    for i in range(1, 10):         # rows
        for j in range(1, 10):     # cols
            
            if i ==1 and 3 <= j :
                print("#", end=" ")

            elif  i == 9 and 3 <= j :
                print("#", end=" ")

            elif j == 1 and i >= 3:
                print("#", end=" ")

            elif   j == 9 and 3 <= i:
                print("#", end=" ")

            # elif  (i,j) in [(2,2),(8,2),(2,8),(8,8)]:
            #     print("#", end=" ")

            else:
                print(" ", end=" ")
        print()

pat()
