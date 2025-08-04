'''
    # # #  
  #       #
#           #
#           #
#           #
  #       #  
    # # #  

'''

def pat():
    for i in range(8):      # rows: 0 to 7
        for j in range(8):  # cols: 0 to 7
            # Top and bottom curves
            if (i == 0 or i == 7) and 2 <= j <= 5:
                print("#", end=" ")
            # Upper and lower sides
            elif (i == 1 or i == 6) and (j == 1 or j == 6):
                print("#", end=" ")
            # Left and right verticals
            elif 2 <= i <= 5 and (j == 0 or j == 7):
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()

pat()