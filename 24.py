
#   * * * * 
# *
# *
#   * * * 
#         *
#         *
# * * * *     


for i in range (1,8,1):
    if i==1 :
        print(" ","* "*4,end="")
    if i==7 :
        print("* "*4,end="")
    if i==4:
        print(" ","* "*3,end="")     
    else:
        if i==2 or i==3:
            print("*",end="")    
        if i==6 or i==5:
            print(" "*7,"*",end="")
    print()