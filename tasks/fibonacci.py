n1=0
n2=1
i=3
num = int(input("Enter the number of lines :"))
if(num==1):
    print(n1)
if(num==2):
    print(n1,"",n2)
if(num>2):
    print(n1,"",n2,end=" ")
    while (i<=num):
        sum=n1+n2
        print(sum,end=" ")
        n1=n2
        n2=sum
        i+=1