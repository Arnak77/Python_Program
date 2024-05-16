#VarLenArgEx_2.py

def disp(*k):
    print(k,type(k))
    for i in k:
        print(i,type(i))

def disp1(*k):
    print("Number of Values:{}".format(len(k)))
    for i in k:
        print(i,end=" ")
    print()
    print("*" * 50)

disp(10,20,30,40)
print("*"*50)

disp(10,20,30)
print("*"*50)

disp(10,20)
print("*"*50)

disp(10)
print("*" * 50)

disp1(10,20,30,40)
disp1(10,20,30)
disp1(10,20)
disp1(10)
