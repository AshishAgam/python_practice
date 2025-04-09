# Dictionary in python

info = {
    "name": "Ashish",
    "age": 23,
    "subjects": ["c", "c++", "Python", "Java"],
    "is_adult": True,
    "marks": 80.89
}

print(info)

print(type(info))

# print specific key's value
print(info["name"])
print(info["subjects"])
print(info["is_adult"])

# change value
info["name"]="ashish"
print(info)

# add another key
info["surname"] = "agam"
print(info)

# Nested Dictionary
student = {
    "name":"Ashish Agam",
    "subject": {
        "c": 98,
        "c++": 87,
        "Java": 85,
        "python":90
    }
}

print(student["subject"]["c"])

# Dictionary Methods
# print all keys and type cast with list
print(list(student.keys()))

# return all values
print(student.values())

# return all (key, val) pairs as tuple
print(student.items())

pairs = (list(student.items()))
print(pairs[0])

# return the key according to value
print(student.get("name2")) # If I entered out of dict key it gives me None

# without using get method 
print(student["name"]) # If I entered out of dict key it gives me error

# insert the specified items to the dictionary
student.update({"city":"Pune"})
print(student)