#Factors_Of_noEx5(forLoop)
n=int(input("Enter a No: "))
if(n<0):
    print("Plz Valid No: ")

for i in range(1,n+1):
    if(n%i==0):
        print("{}".format(i))


print("-"*50)
for i in range(1,(n//2)+1):
    if(n%i==0):
        print("{}".format(i))