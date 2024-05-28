try:
    a=int(input("Enter a no a:"))
    b=int(input("enter a no b:"))
    c=a/b
except ZeroDivisionError:
    print("don't enter zero for deo..")
except ValueError:
    print("don't enter Alphnu,symbols,stars..")
else:
    print("division a & b{}".format(c))
finally:
    print("it's finally block...")