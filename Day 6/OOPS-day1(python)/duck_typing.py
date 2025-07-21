class Person:
    def move(self):
        print("Walking")
class Bike:
    def move(self):
        print("Driving")

def display(a):
    print(a.move())

p=Person()
b=Bike()
p.move()
b.move()