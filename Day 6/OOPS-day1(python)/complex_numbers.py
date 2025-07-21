class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def __add__(self,other):
        return self.real+other.real, self.imaginary+other.imaginary
    def __sub__(self,other):
        return self.real - other.real, self.imaginary-other.imaginary
    def __eq__(self,other):
        return (self.real,self.imaginary) == (other.real,other.imaginary)
c1=Complex(4,5)
c2=Complex(5,6)
print(c1+c2)
print(c1-c2)
print(c1==c2)