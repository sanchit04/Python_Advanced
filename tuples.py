# Tuples are ordered immutable (cannot be modified after instantiation) allows duplicate elements
# it can have any data type elements
# Tuples are created using , (paranthesis) is optional

tuple1="Alex","Gawde",29 # Paranthesis are optional
print(type(tuple1)) #O/P -> <class 'tuple'>

#Creating tuple with single element:
tuple1=("Alex")
print(type(tuple1)) # O/P <class 'str'> (Not correct way of creating tuple,
# tuple needs to be created with atleast 1 comma)

tuple1=("Alex",)
print(type(tuple1)) #OP -> <class 'tuple'>

# Creating tuple from tuple function
tuple1 = tuple([1,2,3,4]) # tuple function takes iterable as a input argument
# , list, sets, string are iterable which are allowed, dict is also allowed but
# only keys with the respective datatype will be stored as elements
print(tuple1) #OP -> (1, 2, 3, 4)

tuple1 = tuple("HelloWorld")
print(tuple1) #OP -> ('H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd')

# When we pass
tuple1 =tuple ({1:"hello"})
print(tuple1[0]) #OP -> 1
print(type(tuple1[0])) #OP -> <class 'int'>

tuple1=tuple(dict(name="Alex",age=35))
print(tuple1) # ('name', 'age') -> keys of dicts are stored
print(type(tuple1[0])) #OP -> <class 'str'>

# accessing tuple elements:

# Using index
tuple1 = tuple ([1,2,3,4,5])
print(tuple1[0]) #OP -> 1

# Accessing index which is not present in tuple
#print(tuple1[10]) #OP -> IndexError: tuple index out of range

# Using negative index
print(tuple1[-1]) #OP -> 5

#print(tuple1[-100]) #OP -> IndexError: tuple index out of range

# ASSIGNING NEW VALUES TO TUPLE:
# Since tuples are immutable this is not supported
#tuple1[0] = "BAC" # OP-> TypeError: 'tuple' object does not support item assignment

# Iterating through tuples

for i in tuple1:
    print(i)
 # OP -> 1
# 5
# 1
# 2
# 3
# 4
# 5

# Checking existing in tuple

if 5 in tuple1:
    print("5 is present!")
else:
    print("not present")

# Length of tuple

print(len(tuple1)) # OP -> 5

# Counting letter inside tuple

tuple1=tuple("hellloworld")
print(tuple1.count("l")) #OP -> 4
print(tuple1.count("p")) #OP -> 0 (it wont fail if not present it will just return 0)

# Getting index of the element in tuple
print(tuple1.index("l")) #OP -> 2 (Gives the first index of occurence for the input letter)

# Gives error if its not present
# print(tuple1.index("p"))
# 0P ->Traceback (most recent call last):
#   File "/Users/sanchitgawde/PycharmProjects/PYTHON_ADVANCED/tuples.py", line 83, in <module>
#     print(tuple1.index("p")) # 0P ->
# ValueError: tuple.index(x): x not in tuple

# Converting tuple to a list
list1=list(tuple1)
print(list1) # OP -> ['h', 'e', 'l', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
print(type(list1)) #OP -> <class 'list'>

# Converting list to a tuple
tuple1=tuple(list1)
print(tuple1) # OP -> ('h', 'e', 'l', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd')
print(type(tuple1)) # OP -> <class 'tuple'>


