class circle:
    def area(self,r):
        self.ac=3.14*r**2
        print("Area of Circle:{}".format(self.ac))

class Square(circle):
    def area(self,s):
        self.sc=s**2
        print("Area of Square:{}".format(self.sc))
        print("--------------------------------------------------------")


class Rect(Square):
    def area(self,l,b):
        self.ra=l*b
        print("Area of Rect:{}".format(self.ra))
        print("--------------------------------------------------------")
        super().area(int(input("Enter a Side:")))
        circle.area(self,int(input("Enter a Radius:")))


c1=Rect()
c1.area(5,6)