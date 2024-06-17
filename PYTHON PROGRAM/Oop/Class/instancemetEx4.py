class sum:
    def cal(self):
        self.a=int(input("Enter a no: "))
        self.b=int(input("Enter a no: "))
    def Add(self):
        self.c=self.a+self.b
    def display(self):
        print("no for a:{}".format(self.a))
        print("no for b:{}".format(self.b))
        print("Add {}+{}={}".format(self.a,self.b,self.c))

s1=sum()
s1.cal()
s1.Add()
s1.display()