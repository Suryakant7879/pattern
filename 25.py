
#   * *   * *   
# *     *     * 
# *           *
#   *       *
#     *   *
#       *


for i in range (1,7,1):
    for j in range (1,8,1):
        if (i==1 and (j==2 or j==3 or j==5 or j==6)) or ((i==2 or i==3) and (j==1  or j==7)) or (i==4 and (j==2 or j==6)) or (i==5 and (j==3 or j==5)) or ((i==6 or i==2) and j==4):
            print("* ",end="")
        else :
            print("  ",end="")
    print()        