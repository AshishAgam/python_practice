# methods in python
# functions are define in class known as method

class Student:
    college_name = "ABC college"
    
    # parameterized constructor
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        
    # method
    def welcome(self):
        print("Welcome to", self.college_name)
        
    def get_marks(self):
        return self.marks
    
    # staticmethod
    @staticmethod
    def hello():
        print("Hello")

s1 = Student("Karan",97)
s1.welcome()
print(s1.get_marks())
s1.hello()


# create class define constructor and calculate average of marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    # define method for calculate average of marks
    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your average score is:", sum/5)

s1 = Student("Karan",[80,90,87,65,56])
s1.avg_marks()

# bank account credit and debit example
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
        
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance:", self.get_balance())
        
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance:", self.get_balance())
    
    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(1500)