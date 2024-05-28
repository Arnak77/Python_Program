

try:
    s1 = input("Enter a No:")
    s2 = input("Enter a No:")
    a = int(s1)
    b = int(s2)
    c = a / b
    print("Division of a & b:{}".format(c))
except ZeroDivisionError:
    print("don't enter zero for deo..")
except ValueError:
    print("don't enter Alphnu,symbols,stars..")