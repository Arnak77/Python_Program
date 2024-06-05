with open("studetinfo","a") as fp:
    print("Enter your data and stop your writting plz press @....")
    while(True):
        kbdata=input()
        if(kbdata!='@'):
            fp.write(kbdata+"\n")
        else:
            break

print("data return to the file....")