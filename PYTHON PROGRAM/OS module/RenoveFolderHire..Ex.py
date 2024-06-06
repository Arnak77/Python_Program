import os
try:
    os.removedirs("D:\Stranger Things\\Arnak\\india\\Ms\\Beed\\Python")
    print("Folder Remove Sucessfully...")
except FileNotFoundError:
    print("Folder Not Found....")