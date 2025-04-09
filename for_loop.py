# for loop in python
nums = [1,5,7,9,66,4,58,66,310,1520]

for val in nums:
    print(val)
    
# using string
x = "Hello"
for char in x:
    print(char)
    
# for loop with else
string = "Learn python"
for char in string:
    if char == "t":
        print("found 't'")
        break
    print(char)
else:
    print("End")
    
# use range function
for el in range(10):
    print(el)
    
for el in range(5,10):
    print(el)
    
for el in range(1,11,3):
    print(el)
    
# calculate sum of upto n
n = int(input("Enter number: "))

sum = 0
for i in range(n+1):
    sum += i
print("Total sum: ",sum)

# calculate factorial of n
n = int(input("Enter number: "))

fact = 1
for i in range(1,n+1):
    fact *= i
print("Factorial of", n,'is',fact)