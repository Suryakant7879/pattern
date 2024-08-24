
# 5 5 5 5 5 
# 5 5 5 5
# 5 5 5
# 5 5
# 5

num=int(input("enter a number"))
for i in range(num,0,-1):
    for j in range(1,i+1,1):
        print(num,end=" ")
    print()