# # function in python
# def print_hello():
#     print("Hello")

# print_hello() # call function

# # Addition of two numbers
# def addition(a,b):
#     return a+b

# sum = addition(10,32)
# print(sum)

# # calculate average of 3 numbers
# def average(a,b,c):
#     sum = a+b+c
#     avg = sum / 3
#     print(avg)
#     return avg
# average(7,8,9)

# # default value / parameter
# def calculation(a=2,b=3):
#     print(a*b)
#     return a*b
# calculation()

# # convert usd to inr
# def convert(usd = int(input("USD: "))):
#     con = usd * 83
#     print("USD: ",usd, "INR: ",con)
# convert()

# # WAF for check number even or odd
# def check_number(num = int(input("Enter number: "))):
#     if num % 2 == 0:
#         print("Number is even")
#     else:
#         print("Number is odd")
# check_number()

# # calculate factorial of n
# def factorial(n = int(input("Enter Number:"))):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print("Factorial is:",fact)
# factorial()

# Recursion
def show(n):
    if(n==0):
        return 0
    print(n)
    show(n-1)
show(3)

# recursive function for calculate sum of n
def cal_sum(n = int(input("Enter n:"))):
    if(n == 0):
        return 0
    return cal_sum(n-1) + n
sum = cal_sum()
print(sum)