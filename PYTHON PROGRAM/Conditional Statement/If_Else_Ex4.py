#word is Vowel word or not
#If_Else_Ex4
word=input("Enter word:")
if ('a'in word.lower() or 'e'in word.lower() or 'i'in word.lower() or 'o'in word.lower() or 'u'in word.lower() ):
    print("{} is Vowel word".format(word))
else:
    print("{} is Not Vowel word".format(word))
