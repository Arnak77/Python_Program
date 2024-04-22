#program for cal  given no---
a=int(input("Enter a number for a="))
m=int(input("Enter a number  for m= "))
n=int(input("Enter a number  for n= "))


#a(m)/a(n)(find)
res=(a**m)/(a**n)
print("="*50)
print("Ans of (a**m)/(a**n)  {},{},{}={}".format(a,m,n,res))
print("="*50)