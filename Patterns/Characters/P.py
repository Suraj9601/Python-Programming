"""
# # # # #
#         #
#         #
# # # # #
#
#
#

"""


def pat():
    for i in range(7):      # rows: 0 to 6
        for j in range(7):  # cols: 0 to 6
            # Top horizontal
            if i == 0 and 0 <= j <= 5:
                print("#", end=" ")
            # Middle horizontal
            elif i == 3 and 0 <= j <= 5:
                print("#", end=" ")
            # Top right curve
            elif (i == 1 or i == 2) and j == 6:
                print("#", end=" ")
            # Left vertical
            elif 0 <= i <= 6 and j == 0:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()

pat()