# Expression Execution
# String and Numeric values can operate together with *
A,B= 2,3
Txt="@"

print(2*Txt*3) # @@@@@@

# String and String can operate with + 
# Concatenation
A,B = "2", 3
Txt = "@"
print((A+Txt)*B) # 2@2@2@

# Numeric values can operate with all arithmetic operators
A,B = 2,3
c=4
print(A+B*c) # 14

# Arithmetic expression with Integer and float will result in float
A,B =10, 5.0
C=A*B
print(C) # 50.0

# Result of division operator with two integers will be float
a,b = 1,2
c=a/b
print(c) # 0.5

# Integer division with float and int will give int displayed as float
a,b = 1.5,3
c=a//b
print(c, a/b) # 0.0, 0.5

# floor gives closest integer, which is lesser than or equal to the float value
# Result of (A//B) is same as floor(A/B)
A,B = 12,5
C=A//B
print(C) # 2

A,B = -12,5
C=A//B   # Actual answer is -2.4
print(C) # -3

# Remainder is negative when denominator is negative
A,B = -5,2
C=A%B
print(C) # 1

A,B = 5,2
C=A%B
print(C) # 1

A,B = 5, -2
C=A%B
print(C) # -1

