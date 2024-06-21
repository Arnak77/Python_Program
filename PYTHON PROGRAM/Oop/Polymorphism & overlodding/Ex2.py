class c1:
    def disc(self):
        print("it is c1 block...")

class c2(c1):
    def disc(self):
        print("it is c2 block...")
        super().disc()

class c3(c2):
    def disc(self):
        print("it is c3 block...")
        super().disc()



o3=c3()
o3.disc()