n=int(input("Enter the number of lines : "))

for i in range(1,n+1):
    x=i
    for j in range(1,i+1):
        print(j,end="")
    while(x>1):
        x-=1
        print(x,end="")
    print("")