#program for cal Simpleint and total amount of int
#SimpleInt.py
p=float(input("Enter a princciple Amount="))
t=float(input("enter Time="))
r=float(input("enter a Rate of Interest="))
#cal sI and total to pay
si=(p*t*r)/100
totalam=p+si
print("="*50)
print("simple princciple Amount={}".format(p))
print("simple Time={}".format(t))
print("simple enter a Rate of Interest={}".format(r))
print("="*50)
print("simple interest cal={}".format(si))
print("TOTAL AMOUNT TO PAY={}".format(totalam))
print("="*50)

