"""2) Take 1 number from user and check 1st and last digit is same or not. 
    num -> 123 
    not same 
    num -> 1231 
    same 
"""
num =int(input("Enter a number to check :"))
last =num%10
while(num>0):
    first =num%10
    num=int(num/10)

if(first==last):
    print("Same")
else:
    print("Not Same!!")