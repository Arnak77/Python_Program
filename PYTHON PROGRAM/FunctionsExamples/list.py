list=[]
n=int(input("How many no you want:"))
if (n<=0):
    print("No is invalid:")

else:
    for i in range (1,n+1):
        val = input("val {} of: ".format(i))
        list.append(val)

    else:
        print(list)