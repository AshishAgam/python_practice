# try except in python

try:
    num1 = int(input("Enter num1:"))
    num2 = int(input("Enter num2:"))

    print(num1 + num2)
    
except Exception as e:
    print("Error: ", str(e))