class c1:
    def __init__(self):
        print("it is c1 default con block...")

class c2(c1):
    def __init__(self):
        print("it is c2 default con block...")
        super().__init__()

class c3(c2):
    def __init__(self):
        print("it is c3 default con block...")
        super().__init__()


o3=c3()
