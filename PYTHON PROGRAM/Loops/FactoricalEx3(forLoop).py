#FactoricalEx3(forLoop).py
n=int(input("Enter A No:"))
if(n<0):
    print("Plz Valid No:")

f=1
for i in range(1,n+1):
    print("{}".format(i))
    f=f*i
print("-"*50)
print("facttorical {}".format(f))
print("-"*50)


