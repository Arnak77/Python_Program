import os
try:
    os.rename("D:\\Stranger Things\\Python","D:\\Stranger Things\\PYT")
    print("Folder Rename Sucessfully....")
except FileExistsError:
    print("Folder Already exist......")