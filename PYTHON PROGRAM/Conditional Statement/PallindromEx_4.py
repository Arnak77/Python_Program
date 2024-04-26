#PallindromEx_4
word=input("Enter word:")
if (word==word[::-1]):
    print("{} is Pallindrom".format(word))
if(word!=word[::-1]):
    print("{} is not Pallindrom".format(word))

