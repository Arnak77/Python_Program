'''
def posno(n):
    if (n>0):
        return True
    else:
        return False
        '''


print("Enter value sperated by space :")
list1=[int(val) for val in input().split()]
print(list1)
l1=tuple(filter(lambda n :n%2==0,list1))
l2=set(filter(lambda n :n%2!=0,list1))
print("*"*50)
print("list valiue:{}".format(list1))
print("Even no:{}".format(l1))
print("Odd no:{}".format(l2))
print("*"*50)

