num=int(input("enter a number of rows= "))
for i in range(1,num+1,1):
    print(" "*(num-i),end="")
    for j in range(1,i+1,1):
        print("*",end="")
    print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end="")
    print()
print()        

for l in range(num,0,-1):
    print(" "*(num-l),end="")
    for m in range(1,l+1,1):
        print("*",end="")
    print(" ",end=" ")
    for n in range(1,l+1,1):
        print("*",end="")
    print() 
