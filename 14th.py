
# 1 2 3 4 5
# 2 2 3 4 5
# 3 3 3 4 5
# 4 4 4 4 5
# 5 5 5 5 5


num=int(input("enter a number of rows= "))
for i in range(1,num+1,1):
    count=1
    sq=1
    for j in range(1,num+1,1):
        if sq<i:
            for k in range(sq,i,1):
              print(i,end=" ")
              count+=1
              sq+=1
        if count<=num:    
            print(count,end=" ")
            count+=1
    print()