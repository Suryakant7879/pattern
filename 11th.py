
# 1 
# 2 3 4 
# 5 6 7 8 9 




num=10
col=1
count=1
for i in range(1,num,1):  
    if count<num:
        for j in range(1,col+1,1):  
            print(count, end=" ")
            count+=1
        col+=2     
        print()    