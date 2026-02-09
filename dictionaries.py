# Key value pairs , unordered and mutables

my_dict={"name":"sanchit","age":34,"hobby":"guitar"}
print(my_dict)
print(type(my_dict))
#OP:
# {'name': 'sanchit', 'age': 34, 'hobby': 'guitar'}
# <class 'dict'>

my_dict=dict(name="sanchit",age=34,hobby="guitar")
print(my_dict)
print(type(my_dict))
#OP:
# {'name': 'sanchit', 'age': 34, 'hobby': 'guitar'}
# <class 'dict'>

#Defining empty dict
my_dict1 = dict()
print(my_dict1) #OP -> {}
print(type(my_dict1)) #OP -> <class 'dict'>

# Accessing values from dict:
# Using keys
print(my_dict["name"]) #OP -> sanchit

# accessing key not available in dict:
#print(my_dict["clan"]) #OP -> KeyError: 'clan'

# Getting all the keys from the dict:
print(list(my_dict.keys())) #OP -> list(dict_keys(['name', 'age', 'hobby'])) -> ['name', 'age', 'hobby']

#Dictionaries are mutable thus we can add and change values in dict
# adding new key to dict:
my_dict["email"]="sachit10gawde@gmail.com"
print(my_dict) # OP -> {'name': 'sanchit', 'age': 34, 'hobby': 'guitar', 'email': 'sachit10gawde@gmail.com'}

# Updating existing key in the dict
my_dict["name"]="Sharvari"
print(my_dict) #OP -> {'name': 'Sharvari', 'age': 34, 'hobby': 'guitar', 'email': 'sachit10gawde@gmail.com'}

# DELETING KEYS FROM DICT:

# using del
del my_dict["age"]
print(my_dict) # OP-> {'name': 'Sharvari', 'hobby': 'guitar', 'email': 'sachit10gawde@gmail.com'}

# using pop
my_dict.pop("email")
print(my_dict)

# using popitem (since 3.7 will remove last key value from the dict)

my_dict.popitem()
print(my_dict)

# CHECK IF KEY EXISTS IN DICTIONARY
# It will do case-insensitive search for key name in my_dict
if "Name" in my_dict:
    print(f"Name key exists in my_dict and its value is:{my_dict['name']}")
else:
    print("not found")

# LOOPING THROUGH DICTIONARY
my_dict=dict(name="sanchit",age=34,hobby="guitar")
# PRINT all keys in the dictionary
for key in my_dict:
    print(key)
#OP:
# name
# age
# hobby

# PRINT all keys second way
for key in my_dict.keys():
    print(key)
#OP:
# name
# age
# hobby

# PRINT all values in a dict:
for value in my_dict.values():
    print(value)

#OP:
# sanchit
# 34
# guitar

# for printing key and values together:

for key,value in my_dict.items():
    print(key,value)
#OP:
# name sanchit
# age 34
# hobby guitar

#ANOTHER WAY OF DOING SAME:

for key in my_dict.keys():
    print(key,my_dict[key])

#OP:
# name sanchit
# age 34
# hobby guitar

