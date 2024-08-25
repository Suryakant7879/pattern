#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *





num=int(input("enter number"))
for i in range(1,num+2,1):
    print(" "*(num-i+1),end="")
    for j in range(1,i+1,1):
        print("*",end=" ")
    print()
for k in range(num,0,-1):
    print(" "*(num-k+1),end="")
    for l in range(1,k+1,1):
        print("*",end=" ")
    print()    
       