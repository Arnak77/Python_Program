#MultiEx_1(for loop).py
n=int(input("Enter a no:"))
if (n<0):
    print("plz valid no:")


print("-"*50)
print("Multiplication Table ")
print("-"*50)

for i in range(1,11):
    print("\t({}*{})={}".format(n,i,n*i))

print("Program exicution compl...")
print("="*50)

