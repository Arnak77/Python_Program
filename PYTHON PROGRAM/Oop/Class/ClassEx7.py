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
s1.no=int(input("Enter a No s1:"))
s1.name=input("Enter a Name s1:")
s1.marks=int(input("Enter Marks s1:"))

s2.no=int(input("Enter a No s2:"))
s2.name=input("Enter a Name s2:")
s2.marks=int(input("Enter Marks s2:"))

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
