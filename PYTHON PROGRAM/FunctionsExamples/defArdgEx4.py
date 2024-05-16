#defArdgEx4.py

def Circleareper(r,pi=3.14):
    ac=pi*r**2
    pc=2*pi*r

    print("*" * 50)
    print("Radius {}".format(r))
    print("Area of Circle {}".format(ac))
    print("Perimeter of Circle {}".format(pc))
    print("*" * 50)


Circleareper(int(input("Entere a Radius:")))