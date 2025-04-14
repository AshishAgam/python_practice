# Multilevel Inheritance in python oop

class A:
    varA = "Welcome To class A"
    
class B:
    varB = "Welcome To class B"
    
class C(A,B):
    varC = "welcome To class C"
    
c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
    