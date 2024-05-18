a=10
b=12
def update():
    #no need to gobal keyword bcoz we are not updatig gobal keyword
    c=a+12
    d=b+23
    print("-" * 50)
    print("c={} and d={}".format(c,d))

#main prgram
print("-"*50)
print("val in main program incr before :a={} and b={}".format(a,b))
update()
print("-"*50)
print("val in main program incr After :a={} and b={}".format(a,b))

