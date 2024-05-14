#ApproachEx_4.py


def mul():#here is called formal parameter
    a= float(input("Enter a no x: "))
    b = float(input("Enter a no y:"))
    #Procss
    c=a*b
    #Result
    return a,b,c
   # print("mul:({},{})={}".format(a,b,c))


#Main Program

a,b,ref=mul()#Function call
print("mul:({},{})={}".format(a,b,ref))
print("*"*50)
ref=mul()
print(ref,type(ref))
print("*"*50)
ref=mul()
print("mul:({},{})={}".format(ref[0],ref[1],ref[2]))