# enter a number of rows= 5
# 5 4 3 2 1 1 2 3 4 5 

# 5 4 3 2     2 3 4 5

# 5 4 3         3 4 5

# 5 4             4 5

# 5                 5



num=int(input("enter a number of rows= "))
c=1
for i in range(num,0,-1):
    n=num
    for j in range(1,i+1,1):  
        print(n,end=" ")
        n-=1
    print(" "*4*(num-i),end="")
    for k in range(1,i+c,1):     
        if k>=c:
            print(k,end=" ")     
    c=c+1        
    print(end="\n \n")        
