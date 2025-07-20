from collections import namedtuple

S1=namedtuple('Student',['name','age','department'])
student=S1('Alice',21,'CSE')
print(student.name)
print(student.age)