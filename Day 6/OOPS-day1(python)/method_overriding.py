class Vehicles:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def move(self):
        print("Moving")

class Car(Vehicles):      # Inheriting from class Vehicles
    def move(self):
        print("Driving")  # Overriding move() method in Vehicles class
class Boat(Vehicles):
    def move(self):
        print("Sailing")
class Plane(Vehicles):
    def move(self):
        print("Flying")

car=Car("Audi",2020)
car.move()
boat=Boat("Ibiza",2021)
boat.move()
plane=Plane("Emirates",2023)
plane.move()