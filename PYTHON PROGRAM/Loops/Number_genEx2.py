#Program for Generating 10 To n a number where n is +ve
#Number_gen_Ex2
n=int(input('Enter a No:'))
print("="*50)
if n<=0:
    print("{} is invalid input..".format(n))

else:
    i=n
    while (i >= 0):
        print("{}".format(i))
        i = i - 1
    print("Program exicution compl...")
print("="*50)
