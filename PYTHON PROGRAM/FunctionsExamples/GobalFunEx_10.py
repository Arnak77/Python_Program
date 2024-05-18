a=10
b=20
c=30
d=40 #a,b,c,d gobal keyword

def oper():
    dict=globals()
    print(dict)
    for v,m in dict.items():
        print(v,"-->",m)
    x=100
    y=200
    z=300
    w=400 #x,y,z,w local variable
    res=x+y+z+w
    print(res)


oper()

