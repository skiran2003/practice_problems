class Temperature:
    def __init__(self,celsius):
        self.__celsius=celsius
    def get_fahrenheit(self):
        if isinstance(self.__celsius,int) or isinstance(self.__celsius,float):
            fahrenheit=(self.__celsius*9/5)+32
            print(fahrenheit)
        else:
            print("Temperature in wrong format!")
    def set_celsius(self,temp):
        if isinstance(temp,int) or isinstance(temp,float):
            self.__celsius = temp

t=Temperature(30)
t.set_celsius(36.2)
t.get_fahrenheit()
