# List Mutable (Modifiable after creation)
# , can have duplicates,
# are ordered in nature (the way elements are added that order is maintatined)
# can have any datatypes stored in same list

#Defining Empty list

list1=[]

# list() takes an iterable object as input
list2=list()

# Defining list with elements
list3=[1,2,4]

print(list1,list2,list3)
print(type(list1),type(list2),type(list3))

# O/P:
# [] [] [1, 2, 4]
# <class 'list'> <class 'list'> <class 'list'>


# Adding new elements to list
# Using append -> will always add element in the last

list1.append("Hello")
list1.append(2)
list1.append(4)
list1.append(5.0)
list1.append(dict(name="ASHER",age=32))
print(f"using append:{list1}")

# using insert -> we can use index input to add element to a specific point
# when we add to a specific index the existing element on that index will move to right! and
# then our new element will be added

list1.insert(3,"I am added here")
print(f"using insert:{list1}")

# If you try to add to the index which is not present in the list
# it will auto add it to the last index for that list
# eg: if i have list with 7 element my last index is 6
# if i do insert(100,"add here") it wont fail it will just add it to index 7

list1.insert(100,"Adding in the last")
print(list1)

# O/P:
# ['Hello', 2, 4, 'I am added here', 5.0, {'name': 'ASHER', 'age': 32}, 'Adding in the last']

# Accessing elements in the list
# using index position
print(list1[0])
print(list1[3])

# O/P
# Hello
# 5.0

# Accessing an index which is not present in the list
# print(list1[10])

#O/P
# Traceback (most recent call last):
#   File "/Users/sanchitgawde/PycharmProjects/PYTHON_ADVANCED/lists.py", line 48, in <module>
#     print(list1[10])
# IndexError: list index out of range

# NEGATIVE INDEXING:
# starts with -1 and from the right
print(list1[-1])


# Iterating through LIST:
for i in list1:
    print(i)

#O/P ->
# Hello
# 2
# 4
# 5.0
# {'name': 'ASHER', 'age': 32}

# Checking item in list (No iterating required to get that!)
if "Hello" in list1:
    print("HELLO PRESENT YAYY!")

# Check the length of list:
print(len(list1)) #O/P -> 5

# Removing items from the list
# using pop method (Last element from the list will be removed)

list1.pop()
print(list1)
#OP : ['Hello', 2, 4, 'I am added here', 5.0, {'name': 'ASHER', 'age': 32}]

# using remove method to remove specific element

list1.remove(2)
print(list1) #OP : ['Hello', 4, 'I am added here', 5.0, {'name': 'ASHER', 'age': 32}]

list1.remove(dict(name='ASHER',age=32))
print(list1) #OP: ['Hello', 4, 'I am added here', 5.0]

# EMPTYING THE LIST
list1.clear()
print(list1) #OP : []

# REVERSE THE LIST
print("Before:",list3)
list3.reverse()
print("After:",list3)
#OP:
# Before: [1, 2, 4]
# After: [4, 2, 1]

# SORTING THE LIST (LIST SHOULD HAVE INT OR FLOAT OR STR TO BE SORTED DICTS CANNOT BE SORTED)
# IF WE ARE SORTING STRING then all list elements should be of type string otherwise will give error
# '<' not supported between instances of 'str' and 'int'
# INT AND FLOAT both present in list , in this case list can be sorted
# list1.append(11)
# list1.append(4.6)
# list1.append(4.0)
# list1.append(3)
# Even if we have all dicts still it cannot be sorted (We need to pass key function using lambda for it to work)
# : TypeError: '<' not supported between instances of 'dict' and 'dict'

list1.append(11)
list1.append(4.6)
list1.append(4.0)
list1.append(3)
print("Before sort",list1)
list1.sort()
print("AFTER sort",list1)
#OP: Before sort [11, 4.6, 4.0, 3]
#   AFTER sort [3, 4.0, 4.6, 11]

# NOTE SORT METHOD MODIFIES THE EXISTING LIST -> If we want to keep the original as is
# and create a new sorted list:

list_sorted=sorted(list1,reverse=True)
print("New SORTED LIST:",list_sorted)
print("Existing list:",list1)

# ADVANCED SORT FOR DICTs

list_dict=list()
list_dict.append(dict(name="Sanchit",age=28))
list_dict.append(dict(name="Yash",age=21))
list_dict.append(dict(name="Papa",age=60))
list_dict.append(dict(name="Mummy",age=54))
list_dict.append(dict(name="Sharvari",age=29))

print("Original list",list_dict)
list_dict_sorted=sorted(list_dict,reverse=True,key=lambda x:x['age'])
print("Sorted List",list_dict_sorted)


