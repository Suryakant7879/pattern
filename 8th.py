
#     *
#    *  *
#   *  *  *
#  *  *  *  *
# *  *  *  *  *


num=int(input("enter number"))
for i in range(1,num+1,1):
    print(" "*(num-i),end="")
    for i in range(1,i+1,1):
        print("*",end="  ")
    print()    