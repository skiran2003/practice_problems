class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello {self.name}! Welcome")

p=Person("Sai",22)
p.greet()