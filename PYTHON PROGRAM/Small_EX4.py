#Small_Three_EX3.py
a=int(input("enter first value of a:"))
b=int(input("enter first value of b:"))
c=int(input("enter first value of c:"))

#logic for big among three
bv = a if a < b and a < c else b if b < c else c if c != a or c != b else "All values are equal"

print("="*50)
print("Small_value({},{},{})={}".format(a,b,c,bv))
print("="*50)

