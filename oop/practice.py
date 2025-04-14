# area of circle and perimeter of circle using class and constructor
# for area of circle define Area() method
# doe perimeter of circle define Perimeter() method

class Circle:
    def __init__(self, redis):
        self.redis = redis
        
    def Area(self):
        return (3.14 * (self.redis ** 2))
    
    def Perimeter(self):
        return (2 * 3.14 * self.redis)
    
r = Circle(21)
print(r.Area())
print(r.Perimeter())


# Example of inheritance
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
        
    def ShowDetails(self):
        print("Role:", self.role)
        print("Department:", self.dept)
        print("Salary:", self.salary)
        
class Engineer(Employee):
    def __init__(self, name, age):
        super().__init__("Engineer", "IT", 500000)
        self.name = name
        self.age = age
        
emp = Engineer("Elon Musk", 40)
emp.ShowDetails()
print("Name:",emp.name) 
print("Age:",emp.age)

# Example of dunder function 
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
    # Use greater than dunder function like __gt__()
    def __gt__(ord1, ord2):
        return ord1.price > ord2.price
    
ord1 = Order("order1", 20)
ord2 = Order("order2", 15)

print(ord1 > ord2) # True