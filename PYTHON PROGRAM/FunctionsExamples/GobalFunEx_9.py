a=10
b=20
c=30
d=40 #a,b,c,d gobal keyword

def oper():
    x=100
    y=200
    z=300
    w=400 #x,y,z,w local variable
    res=x+y+z+w+globals()['a']+globals()['b']+globals()['c']+globals()['d']
    print(res)


oper()
