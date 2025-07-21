class Animal:
    def sound(self):
        print("Making sound")
class Dog(Animal):
    def sound(self):
        print("Barking")

d=Dog()
d.sound()