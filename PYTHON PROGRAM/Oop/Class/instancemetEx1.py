class student:
    def getstudebnt(self):
        self.sno=int(input("Enter a no:"))
        self.sname=input("Enter a name:")
        self.marks=int(input("Enter a marks:"))


s1=student()
s2=student()
s1.getstudebnt()
print("{}".format(s1.__dict__))
print("*"*50)
s2.getstudebnt()
print("{}".format(s2.__dict__))