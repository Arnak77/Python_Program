import os
try:
    os.mkdir("D:\Stranger Things\\Python")
    print("Folder Create Sucessfully....")
except FileExistsError:
    print("Folder Already exist......")