class Sum():pass


s=Sum()
print("-------------------------------------------")
print('content of s1={}'.format(s.__dict__))

print("-------------------------------------------")
s.s1=int(input("Enter a No s1:"))
s.s2=int(input("Enter a No s2:"))
print("{}".format(s.s1))
print("{}".format(s.s2))
print("-------------------------------------------")
s.s3=s.s1+s.s2
print("Add{}+{}={}".format(s.s1,s.s2,s.s3))
