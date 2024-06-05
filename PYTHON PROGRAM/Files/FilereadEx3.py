try:
    with open("Add1","r") as fp:
        filedata=fp.read()
        print("*"*50)
        for i in filedata:
            print(i,end="")

except FileNotFoundError:
    print("file not here...")
