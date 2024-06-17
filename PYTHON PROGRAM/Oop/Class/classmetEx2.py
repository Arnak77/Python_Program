class emp:
    @classmethod
    def getinfo(cls):
        emp.cname="IBM"
        emp.Add="HYD"
    def getstudebnt(self):
        self.sno=int(input("Enter a no:"))
        self.sname=input("Enter a name:")
    def display(self):
        emp.getinfo()
        print("Student no:{}".format(self.sno))
        print("Student name:{}".format(self.sname))
        print("Student cname:{}".format(emp.cname))
        print("Student ADD:{}".format(emp.Add))

e1=emp()
e1.getstudebnt()
e1.display()
print("*"*50)
e2=emp()
e2.getstudebnt()
e2.display()



