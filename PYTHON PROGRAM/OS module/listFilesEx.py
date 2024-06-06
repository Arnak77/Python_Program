import os
fileslist=os.listdir("D:\\NIT\\DATASCIENCE\\ARNAK TASK\\1 to 100\\python 1-100\\FunctionsExamples")
print("List of File")
print("len of files",len(fileslist))
nop=0
nof=0
print("*" * 50)
for lis in fileslist:
    if(lis[-3:]==".py"):
        print(lis)
        nop+=1
print("*" * 50)
print("len of python files:",nop)
print("*" * 50)
print("*" * 50)
for lis in fileslist:
    if(lis[-3:]!=".py"):
        print(lis)
        nof+=1
print("*" * 50)
print("len of not python files:",nof)