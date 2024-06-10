class Student():
    crs="PYTHON"
    city="HYD"


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
print('content of s1={}'.format(s1.crs))
print('content of s1={}'.format(s1.city))


print("*******************************************")
print('content of s2={}'.format(s2.no))
print('content of s2={}'.format(s2.name))
print('content of s2={}'.format(s2.marks))
print('content of s2={}'.format(Student.crs))
print('content of s2={}'.format(Student.city))
print("-------------------------------------------")
