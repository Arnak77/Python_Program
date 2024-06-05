try:
    with open("Add1","r") as fp:
        filedata=fp.readline()
        print("*"*50)
        print(type(filedata))
        print("*"*50)
        print(filedata)
        print("*"*50)
        filedata = fp.readline()
        print(filedata)
        print("*" * 50)

except FileNotFoundError:
    print("file not here...")
