
#       1
#      12
#     123
#    1234
#   12345
#  123456
# 1234567


num=int(input("enter a number"))
n=num
for i in range(1,num+1,1):
    print(" "*(num-i),end="")
    for j in range(1,i+1,1):
        print(j,end="")
    print()    