from abc import ABC,abstractmethod

class TransportMode(ABC):
    def start_engine(self):
        print("Engine Started")
    def stop_engine(self):
        print("Engine Stopped")
    @abstractmethod
    def get_range(self):
        pass

class Car(TransportMode):
    def __init__(self,fuel_remaining,mileage):
        self.fuel=fuel_remaining
        self.mileage=mileage
    def get_range(self):
        return self.fuel * self.mileage

class Bike(TransportMode):
    def __init__(self,fuel_remaining,mileage):
        self.fuel=fuel_remaining
        self.mileage=mileage
    def get_range(self):
        return self.fuel * self.mileage
    
class ElectricScooter(TransportMode):
    def __init__(self,battery_remaining,efficiency):
        self.battery=battery_remaining
        self.efficiency=efficiency
    def get_range(self):
        return self.battery * self.efficiency

c=Car(2,20)
print(c.get_range())
c.stop_engine()
e=ElectricScooter(1,35)
e.start_engine()