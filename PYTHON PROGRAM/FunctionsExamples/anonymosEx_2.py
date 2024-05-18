big=lambda a,b:a if a>b else b if b>a else "Same value"

res=big(float(input("Enter a:")),float(input("Enter b:")))
print(res)