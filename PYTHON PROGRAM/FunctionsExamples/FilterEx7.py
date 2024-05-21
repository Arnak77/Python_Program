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
vowels = set('aeiou')
l1=tuple(filter(lambda word: any(char  in vowels for char  in word.lower()), word))

print("*"*50)
print("Word:{}".format(l1))
print("*"*50)

