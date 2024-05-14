#ApproachEx_1.py


def mul(a,b):#here is called formal parameter
    c=a*b
    return c #herer is local variable

#Main Program
x=int(input("Enter a no x:"))
y=int(input("Enter a no y:"))
ref=mul(x,y)#function call
print("mul:({},{})={}".format(x,y,ref))