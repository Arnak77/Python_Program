import os
try:
    os.makedirs("D:\Stranger Things\\Arnak\\india\\Ms\\Beed\\Python")
    print("Folder Create Sucessfully....")
except FileExistsError:
    print("Folder Already exist......")