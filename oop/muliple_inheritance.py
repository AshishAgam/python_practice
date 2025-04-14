# Multiple Inheritance in python

class Car:
    @staticmethod
    def start():
        print("car started...")
        
    @staticmethod
    def stop():
        print("car stopped...")
        
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, brand, type):
        # use super method
        super().__init__(brand) # call ToyotaCar's constructor
        self.type = type
        
car1 = Fortuner("Toyota","diesel")
print(car1.type)
print(car1.brand)
car1.start()
        