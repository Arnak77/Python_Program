
try:
    Arnak=open("student1","w")
    print("file opened with write mode sucessfully....")
except FileNotFoundError:
    print("FileNotFoundErr...")