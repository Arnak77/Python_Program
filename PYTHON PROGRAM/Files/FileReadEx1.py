try:
    with open("Add1","r") as fp:
        filedata=fp.read()
        print("*"*50)
        print(type(filedata))
        print("*"*50)
        print(filedata)
        print("*"*50)
except FileNotFoundError:
    print("file not here...")
