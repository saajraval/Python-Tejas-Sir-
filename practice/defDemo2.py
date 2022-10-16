# default argument
def sqr(num=0):
    print("Sqr => ",num*num)

def add(a,b=2,c=3,d=4):
    print(a+b+c+d)

sqr(5) # num ->5 
sqr() #num => 0

print("hi")
print("how are you?")
print("Hellow",end="................\t")

add(a=1,c=2,d=3)
add(1,3,4)
