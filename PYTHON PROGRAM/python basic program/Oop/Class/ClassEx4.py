class Student():pass


s1=Student()
s2=Student()

print("-------------------------------------------")
print('content of s1={}'.format(s1.__dict__))
print('content of s2={}'.format(s2.__dict__))
print("-------------------------------------------")
s1.no=11
s1.name="Arnak"
s1.marks=98

s2.no=12
s2.name="Kvr"
s2.marks=99

for i,j in s1.__dict__.items():
    print("{}---->{}".format(i,j))
print("*******************************************")
for i, j in s2.__dict__.items():
    print("{}---->{}".format(i, j))