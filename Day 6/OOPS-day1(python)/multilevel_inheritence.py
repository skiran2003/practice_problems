class GrandParent:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"Hello I am {self.name}"

class Parent(GrandParent):
    pass
    
class Child(Parent):
    pass

gp=GrandParent("grand parent class")
p=Parent("parent class")
c=Child("child class")

print(gp)
print(p)
print(c)