#Program for Sum of Natural Number
#Number_gen_Ex4
n=int(input('Enter a No:'))
print("="*50)
if n<=0:
    print("{} is invalid input..".format(n))




else:

    s=0
    i=1
    while (i<=n):
        print("{}".format(i))
        s =s+i
        i=i+1
    print("=" * 50)
    print("Sum={}".format(s))
    print("Program exicution compl...")
print("="*50)


