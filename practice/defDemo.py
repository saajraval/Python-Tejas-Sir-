# no return no arg 
def add():
    a=int(input("Enter a number :" ))
    b=int(input("Enter a number :" ))
    c= a+b 
    print("SUM :",c)

# no return with arg
def sub(a,b):
    c=a-b
    print("Difference ",c)

# with return no arg
def div():
    a=int(input("Enter a number :" ))
    b=int(input("Enter a number :" ))
    return a/b

# with return with arg
def mul(a,b):
    return a*b;

# add()
# sub(10,3)
# a1=div()
# print("Division :",a1)
# a2=mul(3,4)
# print("Product :",a2)

#keyword argument 
def printMe(name,city,pincode):
    print("name => ",name)
    print("city => ",city)
    print("Pincode => ",pincode)


# printMe("ram","ayodhya",380015)
printMe(pincode=12345,name="laxman",city="Ayodhya")
