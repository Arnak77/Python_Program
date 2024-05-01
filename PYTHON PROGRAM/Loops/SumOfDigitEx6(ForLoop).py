#sum_Of_Given_DigitEx6.py
n=int(input("Enter a No:"))
if(n<0):
    print("Plz Valid No:")

s=0
while(n>0):
    r=n%10
    s=s+r
    n=n//10
print("Sum Of Digit {}".format(s))


