#pallindrom_noEX.py
word=input("enter a world:=")
res="Palliendrome" if word==word[::-1] else "Not Pallidrome"

print("="*50)
print("{} is {}".format(word,res))
print("="*50)



