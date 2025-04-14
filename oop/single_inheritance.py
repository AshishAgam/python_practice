# inheritance in python oop

# Single inheritance

class Car:
    color = "black"
    
    @staticmethod
    def start():
        return ("car started...")
        
    @staticmethod
    def stop():
        return("car stopped...")
        
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name
        
car1 = ToyotaCar("fortuner") 

print(car1.name)
print(car1.color)
print(car1.start())
print(car1.stop())
            