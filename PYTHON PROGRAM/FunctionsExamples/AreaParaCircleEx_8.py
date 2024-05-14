def circleArea():
    r=int(input("Enter radius of Areaof circle "))
    ac=3.14*r**2
    print("Area of circle:{}".format(ac))

def circleparameter():
    r = int(input("Enter radius of Areaof circle "))
    ac = 2*3.14 *r
    print("Area of circle:{}".format(ac))

def AreaofRectangle():
    a = int(input("Enter Value of A: "))
    b = int(input("Enter Value of B: "))
    ar=2 * (a+b)
    print("Area of Rectangle:{}".format(ar))


def meanu():
    print("*" * 50)
    print("1].Area of circle:")
    print("2].parameter of circle:")
    print("3].parameter of circle:")
    print("4].Exit")
    print("*" * 50)

#main program
while(True):
    meanu()
    ch=int(input("Enter your choice:"))
    match(ch):
        case 1:
            circleArea()
        case 2:
            circleparameter()

        case 3:
            AreaofRectangle()


        case 4:
            print("Thx for using this program...")
            break

        case _:
            print("Wrong choice...")