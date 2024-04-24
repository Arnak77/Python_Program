#SwaXOR.py
a=int(input("enter no of a="))
b=int(input("enter no of b="))

print("="*50)
print("original value of a={}".format(a))
print("original value of b={}".format(b))
print("="*50)
#swapping lofic with XOR
a=a^b
b=a^b
a=a^b
print("swapped value of a={}".format(a))
print("swapped value of b={}".format(b))

print("="*50)