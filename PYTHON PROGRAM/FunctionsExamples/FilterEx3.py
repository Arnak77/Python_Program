'''
def posno(n):
    if (n>0):
        return True
    else:
        return False
        '''

print("Enter value sperated by space :")
list1=[int (val) for val in  input().split()]
l1=list(filter(lambda n:n>0,list1))
l2=list(filter(lambda n:n<0,list1))


print("*"*50)
print("print old list:{}".format(list1))
print("print Postive no:{}".format(l1))
print("print Negitive no:{}".format(l2))
print("*"*50)
