
#defArgaEx2.py

def dispstdioinfo(sno,sname,marks,cource="  Python"):
    print("\t{}\t{}\t{}\t{}".format(sno, sname,marks,cource))
def dispstdioinfo1(sno,sname,marks,cource="  Java"):
    print("\t{}\t{}\t{}\t{}".format(sno, sname,marks,cource))

print("*"*50)
print("\tSno\tName\tMarks\tCource")
print("*"*50)

dispstdioinfo(12,"Arnak", 87)#function call
dispstdioinfo(11,"Tanmay",77)#function call
dispstdioinfo(13,"Chetya",89)#function call
dispstdioinfo(14,"Kv r",99)#function call

print("*"*50)
print("\tSno\tName\tMarks\tCource")
print("*"*50)

dispstdioinfo1(15,"Trump",59,"  politics")#function call
dispstdioinfo1(17,"Modi",59,"  politics")#function call
dispstdioinfo1(15,"Russom",59)#function call


print("*"*50)