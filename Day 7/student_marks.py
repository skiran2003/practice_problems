class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self._rollno=rollno
        self.__marks=marks
    def set_marks(self,marks):
        if 0<=marks<=100:
            self.__marks=marks
        else:
            print("Invalid Marks")
    def get_marks(self):
        return self.__marks
    
s=Student("John",22,78)
s.set_marks(-45)
print(s.get_marks())