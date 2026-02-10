# Converting JSON String to python dict This is called as DECODING OR DESERIALIZATION

#JSON LOADS:

import json

#Creating a JSON STRING with dumpts TO SIMULATE
dict1=dict(name="Sanchit",age="32",has_kids=False,address=dict(p_address="kalwa",c_addrss="thane"))
json_str = json.dumps(dict1,indent=4)
print(json_str)
print(type(json_str)) #OP: <class 'str'>

# CONVERT JSON TO DICT using LOADS
dict1=json.loads(json_str)
print(dict1) # OP: {'name': 'Sanchit', 'age': '32', 'has_kids': False, 'address': {'p_address': 'kalwa', 'c_addrss': 'thane'}}
print(type(dict1)) #OP: <class 'dict'>

# USE LOAD to get JSON string from a file and convert to PYTHON DICT
with open('data.json') as f:
    dict1=json.load(f)

print(dict1)
print(type(dict1)) #OP: <class 'dict'>


