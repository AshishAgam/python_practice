# constructor in opp
class Student:
    college_name = "ABC college"
    
    # parameterized constructor
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in database")
    

s1 = Student("Karan",97)
print(s1.name)
print(s1.marks)

s2 = Student("Arjun",80)
print(s2.name)
print(s2.marks)
print(Student.college_name)