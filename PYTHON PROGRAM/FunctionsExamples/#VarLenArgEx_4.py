#VarLenArgEx_4.py

def disp(id,sname,*k,city="Hyd"):

    print("*" * 50)
    print("Student id:{}".format(id))
    print("Student name:{}".format(sname))
    print("Student city:{}".format(city))
    s=0
    for i in k:
        print("\t\t{}".format(i))
        s=s+i
    print("*" * 50)
    print("ToTal:{}".format(s))



disp(100,"Rossum",10,20,30,40,50)
disp(101,"Travis",10,20,30,40)
disp(100,"Kvr",10,20,30)
disp(100,"Dennis",10,20,city="USA")

