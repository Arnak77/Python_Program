
#KeyArgaEx3.py

def dispstdioinfo(sno,sname,marks,cource="  Python"):
    print("\t{}\t{}\t{}\t{}".format(sno, sname,marks,cource))
def dispstdioinfo1(sno,sname,marks,cource="  Java"):
    print("\t{}\t{}\t{}\t{}".format(sno, sname,marks,cource))

print("*"*50)
print("\tSno\tName\tMarks\tCource")
print("*"*50)

dispstdioinfo(12,"Arnak", 87)#function call
dispstdioinfo(cource="  devops",sname="Sonal",marks=90,sno=13)#function call
dispstdioinfo(cource="  Java",marks=100,sname="Jain",sno=11)#function call