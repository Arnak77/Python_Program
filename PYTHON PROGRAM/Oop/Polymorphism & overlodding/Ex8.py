class circle:
    def __init__(self):
        self.r=int(input("Enter a radius:"))
        self.ac=3.14*self.r**2
        print("Area of Circle:{}".format(self.ac))

class Square(circle):
    def __init__(self):
        self.s=int(input("Enter a Side:"))
        self.sc=self.s**2
        print("Area of Square:{}".format(self.sc))
        print("--------------------------------------------------------")
        super().__init__()

class Rect(Square):
    def __init__(self):
        self.l=int(input("Enter a Length:"))
        self.b=int(input("Enter a Breath:"))
        self.ra=self.l*self.b
        print("Area of Rect:{}".format(self.ra))
        print("--------------------------------------------------------")
        super().__init__()

c1=Rect()
