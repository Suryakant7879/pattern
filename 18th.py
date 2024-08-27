# enter a number of row= 6
# * * * * * *
# *       *
# *     *
# *   *
# * *
# *

num=int(input("enter a number of row= "))
for i in range(num,0,-1):
    if i==num:
        print("* "*num,end="")
    else:    
        for j in range(1,i+1,1):
            if (j>=2 and (j>=1 and j<=i-1)):
                print(" ",end=" ") 
            else :
                print("*",end=" ")    
    print()
