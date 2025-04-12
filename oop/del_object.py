# delete object properties or object itself
class Student:
    def __init__(self, name):
        self.name = name
        
s1 = Student("Shradha")
print(s1.name)

# delete
del s1.name
print(s1.name)