class Rectangle:
    def __init__(self,length,breadth):
        self.len=length
        self.bre=breadth
    def perimeter(self):
        return 2*(self.len+self.bre)
    def area(self):
        return self.len*self.bre

r1=Rectangle(20,25)
print(r1.perimeter())
print(r1.area())