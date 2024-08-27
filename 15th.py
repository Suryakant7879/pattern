# enter a number of row= 8
# 1 
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25
# 6 12 18 24 30 36
# 7 14 21 28 35 42 49

num=int(input("enter a number of row= "))
value=1
for i in range(1,num,1):
    value=i
    for j in range(1,i+1,1):
        print(value,end=" ")
        value+=i
    print()