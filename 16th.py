num=int(input("enter a number of row= "))
alpha=65
for i in range(1,num+1,1):
  
    for j in range(1,i+1,1):
        print(chr(alpha),end=" ")
        alpha=alpha+1
    print()    
