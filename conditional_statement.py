# Conditional Statement
light = input("light color: ")

if light == "red":
    print("stop")
elif light == "yellow":
    print("look")
elif light == "green":
    print("go")
else:
    print("light is broken")
    
    
# Single Line if / Ternary Operator
food = input("food: ")
eat = "Yes" if food == "cake" else "No"
print(eat)

food = input("food: ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")

# Cleaver if / Ternary Operator
age = int(input("age: "))
vote = ("yes", "no") [age < 18]
print(vote)

sal = float(input("Salary: "))
tax = sal*(0.1, 0.2) [sal >50000]
print(tax)