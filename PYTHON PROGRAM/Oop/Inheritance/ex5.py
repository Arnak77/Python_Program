class c1:
    def getA(self):
        self.a=int(input("Enter a no for A:"))


class c2(c1):
    def getB(self):
        self.b=int(input("Enter a no for B:"))


class c3(c2):
    def getC(self):
        self.c = int(input("Enter a no for C:"))
    def oper(self):
        self.getA()
        self.getB()
        self.getC()
        self.d=self.a+self.b+self.c
        print("({}+{}+{})={}".format(self.a,self.b,self.c,self.d))

#main program

o3=c3()
o3.oper()

