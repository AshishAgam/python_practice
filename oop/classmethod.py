# @classmethod in python oop

class Person:
    name = "anonymous"
    
    # Normal Method
    # def change_name(self, name):
    #     self.name = name
    
    # Class Method
    @classmethod
    def change_name(cls,name):
        cls.name = name
        
p1 = Person()
print(p1.name)
p1.change_name("Rahul")
print(p1.name)
print(Person.name)