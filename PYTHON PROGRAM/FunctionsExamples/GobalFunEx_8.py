a=10
b=20
c=30
d=40 #a,b,c,d gobal keyword

def oper():
    global a,b,c,d
    res1 = a + b + c + d
    print(res1)
    a=100
    b=200
    c=300
    d=400
    res=a+b+c+d
    print(res)


oper()
