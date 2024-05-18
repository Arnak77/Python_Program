a=10
b=20
c=30
d=40 #a,b,c,d gobal keyword

def oper():
    dict=globals()
    print(dict)
    for v,m in dict.items():
        print(v,"-->",m)
    print("-"*50)
    print("way----1")
    print("val of a",dict['a'])
    print("val of a",dict['b'])
    print("-" * 50)
    print("way----2")
    print("val of a", dict.get('a'))
    print("val of d", dict.get('d'))
    print("-" * 50)
    print("way----3")
    print("val of c", globals()['c'])
    print("val of b", globals()['b'])
    print("-" * 50)
    print("way----2")
    print("val of a", globals().get('a'))
    print("val of d", globals().get('d'))


oper()

