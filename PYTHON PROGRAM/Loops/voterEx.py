#CASE 1:
Age=int(input('Enter Age: '))
if(Age>=18):
    print("valid for voting:")
else:
    print("not valid for voting:")


#CASE 2:
while(True):
    Age = int(input('Enter Age: '))
    if (Age >= 18):
        break
    else:
        print("plz type valid Age:")
print ("{} valid for voting:".format(Age))


#CASE 3:
while(True):
    Age=int(input("Enter a Age:"))
    if(Age>=18 and Age<=100):
        break
    else:
        print("Plz Valid Date:")
print("{} Valid For Voting:".format(Age))


#CASE 4:
while(True):
    Age=int(input("Enter a Age:"))
    if(18<=Age<=100):
        break
    else:
        print("Plz Valid Date:")
print("{} Valid For Voting:".format(Age))