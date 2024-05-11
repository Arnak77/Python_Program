n=int(input("How many tables you want:"))
if (n<0):
    print("invalid input")

lst=list()
for i in range(1,n+1):#outer loop
    num=int(input("enter {} number:".format(i)))
    lst.append(num)

else:
    print("*"*50)
    print("given list of values:{}".format(lst))
    print("*" * 50)
    for num in lst:
        if (num<0):
            print("invalid input:{}".format(num))
        else:

            print("mul table of :{}".format(num))
            print("*" * 50)
            for j in range(1,11):
                print("\t{}*{}={}".format(num,j,num*j))
            else:
                print("*" * 50)









