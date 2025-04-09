marks = [90,95.30,80,85.36,65.32]
print(marks)

# print type
print(type(marks))

# print index wise
print(marks[0])
print(marks[3])

# print length of list
print(len(marks))

# list slicing
print(marks[1:4])

print(marks[-3:-1])

# List methods
lst = [10,5,4,8,9,15]
print(list)

# append method, added one element at the end
lst.append(25)
print(lst)

# sort in ascending order
lst.sort()
print(lst)

# sort in descending order
lst.sort(reverse=True)
print(lst)

# reverse list
lst.reverse()
print(lst)

# insert element at index
lst.insert(2,8)
print(lst)

# remove first occurrence of element
lst.remove(8)
print(lst)

# remove element at index
lst.pop(2)
print(lst)


# WAP to check if a list contain a palindrome of element. (Hint:use copy() method)
list1 = list(map(int,input("Enter numbers separated by space: ").split()))

print(list1)

copy_list1 = list1.copy()
copy_list1.reverse()

if copy_list1 == list1:
    print("Palindrome")
else:
    print("not palindrome")