import os
try:
    os.remove("D:\\Stranger Things\\New folder\\New folder\\text.txt")
    print("File Remove Sucessfully...")
except FileNotFoundError:
    print("File Not Found....")
except PermissionError:
    print("Access id Denied....")