n=int(input("enter a no:"))
if(n<0):
    print("invalid input:")

lst=list()
for num in range(2,n+1):
    c=0
    for i in range(2, num):
        if num % i == 0:
            c = 1
            break
    if (c == 0):
        lst.append(num)



else:
    print("list of prime:")
    for j in lst:
        print("\t{}".format(j))


