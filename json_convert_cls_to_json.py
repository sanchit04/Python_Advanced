# CONVERTING PYTHON CLASS TO JSON
import json


# PYTHON CLASS CANNOT BE DIRECTLY CONVERTED TO JSON!!
class Item:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

item1=Item("Apple",34,2)

# json_str = json.dumps(item1)

#OP: TypeError: Object of type Item is not JSON serializable

# INORDER TO CONVERT TO A JSON STRING WE NEED TO HAVE A PYTHON DICT CREATED FIRST
def encode_item(o):
    if isinstance(o,Item):
        return {'name':o.name,'price':o.price,'quantity':o.quantity}
    return Exception("ENCODE item can only be used for ITEM objects")

# NOW USE THE ABOVE ENCODE FUNCTION IN JSON DUMPS:

json_str = json.dumps(item1,indent=4,default=encode_item)
print(json_str)

#OP:
# {
#     "name": "Apple",
#     "price": 34,
#     "quantity": 2
# }

# ACHIEVING SAME LIKE ABOVE USING CUSTOM JSON ENCODER

from json import JSONEncoder
class UserEncoder(JSONEncoder):

    # Override default method of JSONEncoder parent class
    def default(self,o):
        if isinstance(o,Item):
            return {'name': o.name, 'price': o.price, 'quantity': o.quantity}
        # If its not of instance ITEM then use default JSON encoding!
        return JSONEncoder.default(self,o)

item1=Item("Apple",34,2)
json_str = json.dumps(item1,indent=4,cls=UserEncoder)
print(json_str)
#OP:
# {
#     "name": "Apple",
#     "price": 34,
#     "quantity": 2
# }

dict1 = dict(category='car',brand="honda",model=3455)
json_str = json.dumps(dict1,indent=4,cls=UserEncoder)
print(json_str)

# in the below class default encoder was used thus it worked!
#OP:
# {
#     "category": "car",
#     "brand": "honda",
#     "model": 3455
# }

with open('item.json','w') as f:
    json.dump(dict1,f,indent=4,cls=UserEncoder)