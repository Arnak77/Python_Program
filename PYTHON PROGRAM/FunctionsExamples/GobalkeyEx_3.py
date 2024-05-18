a=10#gobal variable
def incr():
    global  a
    a=a+1

# main program
print("-"*50)
print("val in main program incr before :{}".format(a))
incr()
print("-"*50)
print("val in main program incr After :{}".format(a))
