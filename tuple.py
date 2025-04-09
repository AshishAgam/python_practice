# Tuple
tup = (10,2,56,87,2,2,98,76)
print(tup)
print(type(tup))

# print index wise
print(tup[1])

# in tuple (,) is necessary when we define single value
tup1 = (12,)
print(tup1)
print(type(tup1))

# slicing in tuple
print(tup[2:4])

# methods in tuple
# return index of first occurrence
print(tup.index(2))

# count total occurrences 
print(tup.count(2))