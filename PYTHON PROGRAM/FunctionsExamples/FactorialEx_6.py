#FactorialEx_6.py
def Fact():
    n = int(input("Enter a no:"))
    f = 1
    for i in range(1, n + 1):
        f = f * i
    print("{}".format(f))
    '''if(n<0):
        return "Plz valid no:"  '''

    #else:

Fact()


print("*"*100)
def Fact1(n):

    if(n<0):
        return "Plz valid no:"

    else:

        f=1
        for i in range(1,n+1):
            f=f*i
        return f




n=int(input("input a no:"))
result=Fact1(n)
#result=Fact1(5)
print(result)
