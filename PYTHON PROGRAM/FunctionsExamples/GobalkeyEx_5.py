a=10
b=12
def update():
    global a,b
    a=a+12
    b=b+23

#main prgram
print("-"*50)
print("val in main program incr before :a={} and b={}".format(a,b))
update()
print("-"*50)
print("val in main program incr After :a={} and b={}".format(a,b))

