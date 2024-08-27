
# enter a your name: surya
# s
# su
# sur
# sury
# surya


name=input("enter a your name: ")
for i in range(0,len(name),1):
    for j in range(0,i+1,1):
        print(name[j],end="")
    print()
