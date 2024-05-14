#SimpleIntEx_5.py


def SimpleInt():
    p=int(input("Enter Value of P:"))
    t=int(input("Enter Time:"))
    r=int(input("Rate of Interset:"))
    si=(p*t*r)/100
    totam=si+p
    return p,t,r,si,totam

print("*"*50)
result=SimpleInt()
print(result)
print("*"*50)
p,t,r,si,totam=SimpleInt()
print("*"*50)
print("Principle amount:{}".format(p))
print("Year of time:{}".format(t))
print("Rate Of Interest:{}".format(r))
print("Simple Interset:{}".format(si))
print("Total Amount:{}".format(totam))

