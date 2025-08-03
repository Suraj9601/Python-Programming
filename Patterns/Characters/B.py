'''
# # # # #   
#         # 
#         # 
# # # # #   
#         # 
#         # 
# # # # #   

'''

def pat():
    for i in range(1,8):          
        for j in range(1,7):  
            
            if (i,j) in [(1,6),(4,6),(7,6)]:   
                print(" ", end=" ")
                
            elif j == 1:                    
                print("#", end=" ")
                
            elif i == 1 or i == 4 or i == 7:    
                print("#", end=" ")
                
            elif j == 6:                       
                print("#", end=" ")
                
            else:
                print(" ", end=" ")
        print()

pat()

