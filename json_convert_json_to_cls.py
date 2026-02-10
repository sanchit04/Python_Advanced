# DESERIALIZE JSON STRING TO CLASS OBJECT IN PYTHON
# READING json string from file -> converting that to python class object

import json
class Vehicle:
    def __init__(self,category,brand,model):
        self.category=category
        self.brand=brand
        self.model=model

# json.load or loads both will input a python dict to the decode_vehicle parameter!!
def decode_vehicle(json_dict):
    if "category" in json_dict:
        return Vehicle(json_dict['category'],json_dict['brand'],json_dict['model'])
    return ValueError("decode_vehice should only be used for Vehicle object")

with open('item.json') as f:
    vehicle_obj = json.load(f,object_hook=decode_vehicle)
print(vehicle_obj)
print(type(vehicle_obj))
print(vehicle_obj.brand)

#OP:

# {'category': 'car', 'brand': 'honda', 'model': 3455}
# <__main__.Vehicle object at 0x100f43fd0>
# <class '__main__.Vehicle'>
# honda

# DOING SAME USING JSONDecoder (NOT REALLY NEEDED SHOULD STICK WITH ABOVE IMPLEMENTATION WHICH IS EASY)
from json import JSONDecoder

class VehicleDecoder(JSONDecoder):

    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self,python_dict):
        print(python_dict)
        if "category" in python_dict:
            return Vehicle(python_dict['category'], python_dict['brand'], python_dict['model'])
        return python_dict

with open('item.json') as f:
    vehicle_obj = json.load(f,cls=VehicleDecoder)

print(vehicle_obj)
print(type(vehicle_obj))
print(vehicle_obj.brand)

# OP:
# {'category': 'car', 'brand': 'honda', 'model': 3455}
# <__main__.Vehicle object at 0x100f43fd0>
# <class '__main__.Vehicle'>
# honda

