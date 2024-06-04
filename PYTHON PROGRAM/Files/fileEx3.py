
try:
    Arnak=open("student1","r")
except FileNotFoundError:
    print("FileNotFoundError......")

else:
    print("File Opened With Read Mode Sucessfully.....")