# private attribute in python oop
# private attribute we can not use out of class
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # this ia a private attribute
    
    # access private attribute
    def reset_pass(self):
        return(self.__acc_pass)
        
acc1 = Account("123456", "abcd")
print(acc1.acc_no)
print(acc1.reset_pass())

# private method
class Person:
    __name = "anonymous"
    
    def __hello(self):
        return "hello person"
    
    def Welcome(self):
        return self.__hello() # __hello method use in class
        
p1 = Person()
print(p1.Welcome())
# print(p1.__hello) # this is give me error because __hello method is private