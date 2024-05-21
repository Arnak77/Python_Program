def posno(n):
    if (n>0):
        return True
    else:
        return False

print("Enter value sperated by space :")
list1=[int (val) for val in  input().split()]
l1=list(filter(posno,list1))
print("*"*50)
print("print old list:{}".format(list1))
print("print Postive no:{}".format(l1))
print("*"*50)
