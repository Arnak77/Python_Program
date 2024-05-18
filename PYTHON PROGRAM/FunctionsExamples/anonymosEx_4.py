pall=lambda word:"word is pall" if word==word[::-1] else "not pall"
print(pall("MoM"))
