class emp:
    def __init__(self):
        print("Constructoe")
        self.eno=12
        self.ename="Arnak"

e1=emp()
print("content of e1={}".format(e1.__dict__))