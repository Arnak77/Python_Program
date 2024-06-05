scrfile=input("Enter source file: ")
try:
    with open(scrfile,"r") as rp:
        dsfile=input("destinaction file:")
        with open(dsfile,"a") as wp:
            scrfile=rp.read()
            wp.write(scrfile)
            print("Data is copy...")
except FileNotFoundError:
    print("Plz Valid File Name....")