with open("Student2","w") as fp:
    print("File open with write mode...")
    print("File name:",fp.name)
    print("File mode:", fp.mode)
    print("File readable:", fp.readable())
    print("File writeable:", fp.writable())
    print("File closed:", fp.closed)
print("out of with open file.....")
print("File closed:", fp.closed)
