#Program for Product  of Natural Number
#ProductNoEx7
n=int(input("Enter a no:"))
if(n<0):
    print("{} invalid input".format(n))
else:
    i=1
    f=1
    while(i<=n):
        print("{}".format(i))
        f=f*i
        i=i+1
    print("=" * 50)
    print("Product={}".format(f))

















