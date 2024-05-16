#defArgaEx1.py
def dispstdioinfo(sno,sname,marks,cource="  Python"):
    print("\t{}\t{}\t{}\t{}".format(sno, sname,marks,cource))

print("*"*50)
print("\tSno\tName Marks Cource")
print("*"*50)

dispstdioinfo(12,"A", 87)#function call
dispstdioinfo(11,"S",77)#function call
dispstdioinfo(13,"$",89)#function call
print("*"*50)