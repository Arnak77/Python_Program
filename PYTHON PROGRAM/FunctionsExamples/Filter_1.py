

def posno(n):
    if (n>0):
        return True
    else:
        return False

list1=[12,23,34,-65,-3,-43,23]
l1=list(filter(posno,list1))
print("*"*50)
print("print old list:{}".format(list1))
print("print Postive no:{}".format(l1))
print("*"*50)
