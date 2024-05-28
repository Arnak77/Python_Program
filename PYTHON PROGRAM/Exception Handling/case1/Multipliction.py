from zeroErr1 import ZeroDivError,ValueError
def mul(n):
    if (n==0):
        raise ZeroDivError
    elif (n<0):
        raise ValueError
    else:
        print("*"*50)
        print("Mult Table: ")
        print("*" * 50)
        for i in range(1,11):
            print("mul({}*{}):{}".format(n,i,n*i))
        print("*" * 50)