# COPYING A DICTIONARY

my_dict=dict(name="Sanchit",age=23,hobby="guitar")
copy_dict=my_dict # Assignment operator does not create a new dict object it just creates a reference still pointing to old dict objhect
print("COPY DICT before:",copy_dict)
print("Original Dict before:",my_dict)

copy_dict["name"]="Sharvari"
print("COPY DICT after:",copy_dict)
print("Original Dict after:",my_dict)

# TO FIX THIS
# using dict function
my_dict=dict(name="Sanchit",age=23,hobby="guitar")
copy_dict = dict(my_dict) # use dict function
copy_dict["name"]="Sharvari"
print("COPY DICT with dict():",copy_dict)
print("Original with dict()",my_dict)

# OR using shallow copy
import copy
copy_dict = copy.copy(my_dict)
copy_dict["name"]="Sharvari"
print("COPY DICT with copy():",copy_dict)
print("Original with copy()",my_dict)

# MERGING TWO DICTIONARIES:
dict1=dict(name="Sanchit",age=34,hobby="guitar")
dict2={1:"hello",2:"world","name":"Yash"}

dict1.update(dict2)
print(dict1)
#OP : {'name': 'Yash', 'age': 34, 'hobby': 'guitar', 1: 'hello', 2: 'world'}
# If a key is present in dict1 as well as dict2 then dict1 key will be updated with value of dict2
# If a key is not present in dict1 but presnt in dict2 then dict2 key will be added to dict1
# If a key is present in dict1 but not in dict2 , result will have that key in dict1

#POSSIBLE KEY DATATYPES in Dictionary
#Supports immutable datatypes : string, int, tuples
# Does not support list since its mutable

# TUPLE AS A KEY
dict1={("Hello","World"):3}
print(dict1) #OP: {('Hello', 'World'): 3}

# INT AS A KEY
dict1={1:"Hello"}
print(dict1) #OP: {1: 'Hello'}

# STR as a KEY
dict1={"temp":"hello"}
print(dict1) #OP: {'temp': 'hello'}

# LIST as a KEY
dict1={[2,3,4]:"hello"}
print(dict1)

#OP:
# Traceback (most recent call last):
#   File "/Users/sanchitgawde/PycharmProjects/PYTHON_ADVANCED/dictionary_advanced.py", line 55, in <module>
#     dict1={[2,3,4]:"hello"}
# TypeError: unhashable type: 'list'
