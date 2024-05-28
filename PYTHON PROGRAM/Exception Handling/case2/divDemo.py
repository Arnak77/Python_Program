from Division import divop
from ZeroErr import ZerodivError
a=int(input("Enter no for A:"))
b=int(input("Enter no for B:"))

try :
    res=divop(a,b)
    print("div A & b:{}".format(res))
except ZerodivError:
    print("don't enter zero for deo..")