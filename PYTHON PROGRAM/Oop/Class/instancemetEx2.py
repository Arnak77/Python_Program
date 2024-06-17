class student:
    def getstudebnt(self):
        self.sno=int(input("Enter a no:"))
        self.sname=input("Enter a name:")
        self.marks=int(input("Enter a marks:"))

    def display(self):
        print("Student no:{}".format(self.sno))
        print("Student name:{}".format(self.sname))
        print("Student marks:{}".format(self.marks))




s1=student()
s2=student()
s1.getstudebnt()
print("*"*50)
s2.getstudebnt()
s1.display()
print("*"*50)
s2.display()
