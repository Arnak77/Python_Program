'''
def posno(n):
    if (n>0):
        return True
    else:
        return False
        '''


line=input("Enter Line of text :")
word=line.split()
print("*"*50)
print(word)
l1=tuple(filter(lambda word:len(word)>=3,word))

print("*"*50)
print("Word whose len greater than 3:{}".format(l1))
print("*"*50)

