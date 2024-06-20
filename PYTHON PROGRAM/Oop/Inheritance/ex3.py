class c1:
    def disc1(self):
        print("c1-display")
class c2(c1):

    def disc2(self):
        self.disc1()
        print("c2-display")


o2=c2()
o2.disc2()