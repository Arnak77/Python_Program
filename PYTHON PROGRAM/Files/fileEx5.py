try:
    with open("Student2","r") as fp:
        print("File Opened With Read Mode Sucessfully.....")
except FileNotFoundError:
    print("FileNotFoundError......")

