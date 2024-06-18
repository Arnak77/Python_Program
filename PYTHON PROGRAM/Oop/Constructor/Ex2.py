class emp:
    def __init__(self,en,ename):
        self.en=en
        self.ename=ename



e1=emp(100,"Russum")
print("{}".format(e1.__dict__))