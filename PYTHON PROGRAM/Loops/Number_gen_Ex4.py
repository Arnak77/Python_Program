#Program for Generating Multiplction table
#Number_gen_Ex4
n=int(input('Enter a No:'))
print("="*50)
if n<=0:
    print("{} is invalid input..".format(n))

else:
    i=1
    while (i <= 10):
        print("{}*{}={}".format(n,i,n*i))
        i = i+1
    print("Program exicution compl...")
print("="*50)


