#Even_Odd_NOEx4(ForLoop)
n=int(input("Enter A no:"))
if(n<0):
    print("Plz Valid No:")

print("Even No:")
for i in range(2,n+1,2):
    print("{}".format(i))
print("-"*50)

print("Odd No:")
for i in range(1,n+1,2):
    print("{}".format(i))
print("-"*50)


print("Program exicution compl...")