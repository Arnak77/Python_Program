class Student():pass


s1=Student()
s2=Student()
print("Before Adding.....")
print("-------------------------------------------")
print('content of s1={}'.format(s1.__dict__))
print('content of s2={}'.format(s2.__dict__))
print("-------------------------------------------")
print("After Adding......")
s1.no=11
s1.name="Arnak"
s1.marks=98

s2.no=12
s2.name="Kvr"
s2.marks=99
print("-------------------------------------------")
print('content of s1={}'.format(s1.no))
print('content of s1={}'.format(s1.name))
print('content of s1={}'.format(s1.marks))
print("*******************************************")
print('content of s2={}'.format(s2.no))
print('content of s2={}'.format(s2.name))
print('content of s2={}'.format(s2.marks))
print("-------------------------------------------")
