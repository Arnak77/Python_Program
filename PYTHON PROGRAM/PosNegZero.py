#PosNegZero.py
n=int(input("enter value:"))
res="NO IS POSITIVE" if n>0 else "NO IS NEGITIVE" if n<0 else "NO IS ZERO"
print("="*50)
print("({})={}".format(n,res))
print("="*50)