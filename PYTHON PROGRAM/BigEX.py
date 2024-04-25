#Program for Finding Biggest of Two no and cheack equality
#BigEX1.py
a=int(input("enter first value:"))
b=int(input("enter first value:"))


# logic for finding Biggest
bv=a if a>b else b
print("="*50)
print("Big_value ({},{})={}".format(a,b,bv))
print("="*50)