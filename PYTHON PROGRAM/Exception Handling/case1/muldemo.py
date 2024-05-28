from Multipliction import mul
from zeroErr1 import ZeroDivError,ValueError
try:
    n=int(input("Enter A no:"))
    mul(n)
except ZeroDivError:
    print("don't input Zero...")
except ValueError:
    print("Don't input -ve no..")
