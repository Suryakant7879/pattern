# enter a number of rows= 5
#      *
#     * *
#    *   *
#   *     *
#  *       *
# *         *
#  *       *
#   *     *
#    *   *
#     * *
#      *



num=int(input("enter a number of rows= "))
for i in range(1,num+2,1):
    print(" "*(num-i+1),end="")
    for j in range(1,i+1,1):
        if j==1 :
            print("*",end=" ")
        else:
            if i==j:
                print("*",end=" ")
            else:    
               print(" ",end=" ") 
    print()    
for i in range(num,0,-1):
    print(" "*(num-i+1),end="")
    for j in range(1,i+1,1):
        if j==1:
            print("*",end=" ")
        else:
            if i==j:
                print("*",end=" ")
            else:    
               print(" ",end=" ")  
    print()    
        
