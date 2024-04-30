#Program for Square Sum of Natural Number
#SquareSumNaturalNoEx4
n=int(input("Enter a no:"))
if(n<0):
    print("{} invalid input".format(n))

else:
    i=1
    ss=0
    s=0
    while(i<=n):
        print("{} \t\t{} ".format(i,i**2))
        s=s+i
        ss=ss+i*i
        i=i+1
    print("=" * 50)
    print("{} \t\t{}".format(s,ss))

    print("Program exicution compl...")



















