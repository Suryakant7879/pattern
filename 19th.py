#    enter a number of rows= 5


#    * * * * *
#    *       *
#    *       *
#    *       *
#    * * * * *


num=int(input("enter a number of rows= "))
for i in range(1,num+1,1):
    for j in range(1,num+1,1):
        if i==1 or j==1:
            print("*",end=" ")
        else:
            if i==num or j==num:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()        