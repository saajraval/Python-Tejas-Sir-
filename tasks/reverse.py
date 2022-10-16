a = int(input("Enter a number to reverse : "))
rev=0

while a>0 :
    x = a%10
    rev = rev *10  +x 
    a=int(a/10) 

else:
    print(rev)

