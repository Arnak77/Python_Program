#primeNumberEx7.py
n=int(input("Enter A no:"))
if (n<0):
    print("Plz Valid No:")

c=1
for i in range(2,n):
    if (n%i==0):
        c=0
        break
if(c==1):
    print("{} No is Prime".format(n))
else:
    print("{} No is Not Prime".format(n))


