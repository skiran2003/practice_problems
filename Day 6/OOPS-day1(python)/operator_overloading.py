class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages + other.pages
b1=Book(150)
b2=Book(275)
print(b1+b2)
