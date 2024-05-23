from Aopmeu import meanu
from Aopimpl import *
while(True):
    meanu()
    ch = int(input("Enter Your Choice:"))
    match (ch):
        case 1:
            add()
        case 2:
            sub()
        case 3:
            mul()
        case 4:
            ndiv()
        case 5:
            floordiv()
        case 6:
            moduladiv()
        case 7:
            expoentitation()

        case 8:
            print("Thx fro using Program")
            break
        case _:
            print("Plz Give Valid Case......")



