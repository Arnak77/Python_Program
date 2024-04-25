#Program for Finding Biggest of Two no and cheack equality
#BigEX2.py
a=int(input("enter first value:"))
b=int(input("enter first value:"))


# logic for finding Biggest and for equality
bv=a if a>b else b if b>a else "Values are Equal..."
print("="*50)
print("Big_value ({},{})={}".format(a,b,bv))
print("="*50)