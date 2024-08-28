# enter a number of rows= 5
# *         *
# **       **
# ***     ***
# ****   ****
# ***** *****

num=int(input("enter a number of rows= "))
for i in range(1,num+1,1):
    for j in range(1,i+1,1):
        print("*",end="")
    print(" "*2*(num-i),end=" ")    
    for k in range(1,i+1,1):
        print("*",end="")
    print()    
   