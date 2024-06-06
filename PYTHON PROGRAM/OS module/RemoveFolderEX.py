import os
try:
    os.rmdir("D:\Stranger Things\\Python")
    print("Folder Remove Sucessflly...")
except FileNotFoundError:
    print("Folder Does not Exist....")
except FileExistsError:
    print("Folder Does not Exist....")