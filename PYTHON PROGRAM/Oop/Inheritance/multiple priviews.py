class univercity:
    def univercity(self):
        self.uname=input("Enter a univercity Name:")
        self.uadd=input("Enter a univercity Add:")
    def disudel(self):
        print("univercity Name:{}".format(self.uname))
        print("univercity Add:{}".format(self.uadd))

class collage(univercity):
    def collage(self):
        self.cname=input("Enter a collage Name:")
        self.cadd=input("Enter a collage Add:")
    def discdel(self):
        print("collage Name:{}".format(self.cname))
        print("collage Add:{}".format(self.cadd))

class student(collage):
    def student(self):
        self.sname=input("Enter a student Name:")
        self.sadd=input("Enter a student Add:")
        self.sno=int(input("Enter Student No:"))

    def dissdel(self):
            print("student Name:{}".format(self.sname))
            print("student Add:{}".format(self.sadd))
            print("Student No:{}".format(self.sno))


c1=student()
c1.univercity()
c1.collage()
c1.student()
c1.disudel()
c1.discdel()
c1.dissdel()