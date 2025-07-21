class Father:
    def __init__(self):
        self.hobbies="Gardening"
    def traits(self):
        return f"Father hobbies are: {self.hobbies}"
class Mother:
    def __init__(self):
        self.hobbies="Cooking"
    def traits(self):
        return f"Mother hobbies are: {self.hobbies}"
class Child(Father,Mother):
    def traits(self):
        Father.traits(self)
        Mother.traits(self)
c=Child()
print(c.traits())