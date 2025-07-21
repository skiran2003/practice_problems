class Student:
    def __init__(marks,math,phy,bio):
        marks.math=math
        marks.phy=phy
        marks.bio=bio
    def get_average(marks):
        return (marks.math + marks.phy + marks.bio)/3

s1=Student(91,87,95)
print(s1.get_average())