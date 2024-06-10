class SimpleInt():pass


s1=SimpleInt()
s1.p=float(input("Enter a princciple Amount="))
s1.t=float(input("enter Time="))
s1.r=float(input("enter a Rate of Interest="))
s1.si=(s1.p*s1.t*s1.r)/100
s1.tot=s1.si+s1.p
print("="*50)
print("simple princciple Amount={}".format(s1.p))
print("simple Time={}".format(s1.t))
print("simple enter a Rate of Interest={}".format(s1.r))
print("="*50)
print("simple interest cal={}".format(s1.si))
print("TOTAL AMOUNT TO PAY={}".format(s1.tot))
print("="*50)