#Program for Generating 1 To n a number where n is +ve
#Number_gen_Ex
n=int(input('Enter a No:'))
print("="*50)
if n<=0:
    print("{} is invalid input..".format(n))

else:
    i=1
    while (i <= n):
        print("{}".format(i))
        i = i + 1
    print("Program exicution compl...")
print("="*50)
