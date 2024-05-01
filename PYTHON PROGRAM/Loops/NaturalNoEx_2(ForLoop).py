#Program for Square Sum of Natural Number
#SquareSum_And_Cube_NaturalNoEx_2
n=int(input("Enter A no:"))
if(n<0):
    print("Plz Valid No:")
print("-"*50)
s=0
ss=0
sss=0
for i in range(1,n+1):
    print("{} \t\t{} \t\t{}".format(i,i*i,i**3))
    s=s+i
    ss=ss+i**2
    sss=sss+i**3
print("-"*50)
print("{} \t\t{} \t\t{}".format(s,ss,sss))