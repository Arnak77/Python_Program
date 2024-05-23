def add():
    print("Enter two values for add:")
    a,b=int(input()),int(input())
    print("({}+{})={}".format(a,b,a+b))

def sub():
    print("Enter two values for sub:")
    a, b = int(input()), int(input())
    print("({}+{})={}" .format(a,b,a-b))

def mul():
    print("Enter two values for mul:")
    a, b = int(input()), int(input())
    print("({}+{})={}".format(a,b,a*b))

def ndiv():
    print("Enter two values for div:")
    a, b = int(input()), int(input())
    print("({}+{})={}".format(a,b,a/b))

def floordiv():
    print("Enter two values for fioor div:")
    a, b = int(input()), int(input())
    print("({}+{})={}".format(a,b,a//b))

def moduladiv():
    print("Enter two values for modula dinv:")
    a, b = int(input()), int(input())
    print("({}+{})={}".format(a,b,a%b))

def expoentitation():

    a, b = int(input("Enter base")), int(input("Enter Power"))
    print("({}+{})={}".format(a,b,a**b))
