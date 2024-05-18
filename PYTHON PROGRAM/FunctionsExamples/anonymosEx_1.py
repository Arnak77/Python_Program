# Anonymous function
print("*"*50)
def dum(a,b):
    c=a+b
    return c

res=dum(2,4)
print(res)
print("*"*50)


print("*"*50)
print("Anonymos function")
add=lambda a,b:a+b

res=add(4,3)
print(type(add))
print(res)
print("*"*50)