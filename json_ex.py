"""
EG JSON OBJECT:

{
"name":"Sanchit",
"hobby":"Guitar",
"has_work": true
"age":30
"expertise":[
    {"skill":"python","expertise":"good"},
    {"skill":"agentic ai","expertise":"excellent"}
],
"addresses":{"current_address":"Piramal Vaikunth","permanent_address":"Shree Kedar"}
}
"""
# JSON DUMP AND DUMPS IS USED FOR ENCODING or SERIALIZATION of PYTHON DICT

# CONVERT PYTHON DICT TO JSON STRING
import json

dict1=dict(name="Sanchit",age="32",has_kids=False,address=dict(p_address="kalwa",c_addrss="thane"))
print(dict1)
#OP: {'name': 'Sanchit', 'age': '32', 'has_kids': False, 'address': {'p_address': 'kalwa', 'c_addrss': 'thane'}}

json_str = json.dumps(dict1)
print(json_str)
# Notice how has_kids boolean value has changed to json way of defining booleans in output
# OP: {"name": "Sanchit", "age": "32", "has_kids": false, "address": {"p_address": "kalwa", "c_address": "thane"}}

# JSON DUMPS WITH INDENTATION
json_str = json.dumps(dict1,indent=4)
print(json_str)
# OP: {
#     "name": "Sanchit",
#     "age": "32",
#     "has_kids": false,
#     "address": {
#         "p_address": "kalwa",
#         "c_addrss": "thane"
#     }
# }

# JSON DUMPS with sorted keys
json_str = json.dumps(dict1,indent=4,sort_keys=True)
print(json_str)
#OP: {
#     "address": {
#         "c_addrss": "thane",
#         "p_address": "kalwa"
#     },
#     "age": "32",
#     "has_kids": false,
#     "name": "Sanchit"
# }

# JSON DUMPS with change in seperator (NOT RECOMMENDED PRACTISE)
json_str = json.dumps(dict1,indent=4,separators=(";","="))
print(json_str)

#OP:
# {
#     "name"="Sanchit";
#     "age"="32";
#     "has_kids"=false;
#     "address"={
#         "p_address"="kalwa";
#         "c_addrss"="thane"
#     }
# }

