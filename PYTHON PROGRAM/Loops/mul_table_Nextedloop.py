n=int(input("enter a no="))
if (n<0):
    print("invalid input")

for i in range(1,n+1):#outer loop
    print("multiplaction table for {}".format(i))
    print("*"*50)
    for j in range(1,11):#inner loop
        print("mult {}*{}={}".format(i, j, i * j))
    else:
        print("=" * 100)




