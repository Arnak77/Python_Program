#Program for LineOfWord
#LineOfWords7.py
line=input("Enter Line Of Text:")
print("{}".format(line))
print("=" * 50)
words=line.split()
print("{}".format(words))
print("=" * 50)
print("len of words={}".format(len(words)))
print("=" * 50)
i=0
while(i<len(words)):
    print("{} \t\t{}".format(words[i],len(words[i])))
    i=i+1
print("=" * 50)

































