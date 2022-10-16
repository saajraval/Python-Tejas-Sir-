# varargs
# varaible length argument

def add(*n):
    sum = 0
    for x in n : 
        sum =sum+x
    print("Add = ",sum)

add(1,2,3) 
add(1,2,3,4)