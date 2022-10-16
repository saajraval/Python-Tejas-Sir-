# create one function max that accept three arguments and return
# max from three args. 
# now use that max num in oddEven function that return 1 if number 
# is odd and 0 if number is even. 

x = int(input("Enter 1st number :"))
y = int(input("Enter 2nd number :"))
z = int(input("Enter 3rd number :"))


def max(a=x,b=y,c=z):
    if a>b : 
        if a>c :
            return a
        else:
            return c
    else:
        if b>c :
            return b
        else:
            return c

ans = max()
def oddEven(a=ans):
    if(a % 2 ==0):
        return 0 
    else :
        return 1

op = oddEven()
print("The answer is : -> ",op)