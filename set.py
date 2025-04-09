# set in python
collection = {20,2,3,4,5,6,7,7,2,"hello",78}
print(collection)
print(type(collection))

# print total number of items
print(len(collection))

# create empty set
set1 = set()
print(set1)
print(type(set1))

# Set Methods
# add an element
set1.add(21)
set1.add("Apple")
set1.add("s")
print(set1)

# remove the element
set1.remove("Apple")
print(set1)

# empties the set
set1.clear()
print(set1)

# removes a random value
print(collection.pop())
print(collection)

# combine both set values and return new
set2 = {10,20,30}
set3 = {30,40,50}

print(set2.union(set3)) # {10,20,50,40}

# combine common value and return new
print(set2.intersection(set3)) # {30}

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)
print(type(values))