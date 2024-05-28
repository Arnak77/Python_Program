#Gereating Exeption div by Zero
from ZeroErr import ZerodivError
def divop(a,b):
    if(b==0):
        raise ZerodivError
    else:
        return (a/b)

divop(12,6)