

# 1
# 3 3
# 5 5 5
# 7 7 7 7
# 9 9 9 9 9


num=int(input("enter a number of rows= "))
count=1
for i in range(1,num+1,1):
    for i in range(1,i+1,1):
        print(count,end=" ")
    count+=2
    print()