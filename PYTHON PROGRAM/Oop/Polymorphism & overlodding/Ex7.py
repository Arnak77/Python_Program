class circle:
    def area(self):
        self.r=int(input("Enter a radius:"))
        self.ac=3.14*self.r**2
        print("Area of Circle:{}".format(self.ac))

class Square():
    def area(self):
        self.s=int(input("Enter a Side:"))
        self.sc=self.s**2
        print("Area of Square:{}".format(self.sc))
        print("--------------------------------------------------------")


class Rect(Square,circle):
    def area(self):
        self.l=int(input("Enter a Length:"))
        self.b=int(input("Enter a Breath:"))
        self.ra=self.l*self.b
        print("Area of Rect:{}".format(self.ra))
        print("--------------------------------------------------------")
        super().area()
        circle.area(self)

c1=Rect()
c1.area()