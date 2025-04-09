str1 = "ashish"
print(str1)

str2 = 'this is string'
print(str2)

str3 = '''this is another string'''
print(str3)

str4 = """this is string using double code"""
print(str4)

str5 = "I don't know"
print(str5)

str6 = "In string use \n for move string to separate line"
print(str6)

str7 = "In string \t use for more space like tab"
print(str7)

str8 = "Hello"
str9 = "World"
result = str8 + " " + str9
print(result)

# print length of string  
print(len(result))

# print index of specific character
print(result[4])

# Slicing of string
print(result[0:5])
print(result[5:])
print(result[:-1])
print(result[-4:-1])

# String functions
str = "i am studying python"
# return true if string ends with substr
print(str.endswith("on"))

# capitalize first character
print(str.capitalize())

# replace all occurrences of old
print(str.replace("y", "e"))

# return first index of first occurrer
print(str.find("a"))

# count the occurrence of substr
print(str.count("n"))