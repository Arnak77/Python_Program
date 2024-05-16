#KeyArdgEx2.py

def keyArg(a,b,c,d):
    print("\t{}\t{}\t{}\t{}".format(a,b,c,d))



print("*" * 50)
print("\tA\tB\tC\tD")
print("*" * 50)

keyArg(10,20,30,40)
keyArg(b=20,c=30,a=10,d=40)
keyArg(d=40,b=20,c=30,a=10)
keyArg(10,20,d=40,c=30)
print("=" * 50)