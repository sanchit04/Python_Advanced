# JSON DUMPS -> Converts python dict to json string : returns a string object
# JSON DUMP -> Converts pythong dict to json string and write to a file , it requires a file object to work

import json

dict1=dict(name="Sanchit",age="32",has_kids=False,address=dict(p_address="kalwa",c_addrss="thane"))
print(dict1)

# dumps -> returns a json string
json_str = json.dumps(dict1,indent=4)
print(json_str)

# Here in dump file object pass to dump method is mandatory
with open('data.json','w') as f:
    json.dump(dict1,f,indent=4)

# double encodes the json and stores as a string literal
with open('bad.json','w') as f:
    json.dump(json_str,f,indent=4)

#OP from FILE:
#"{\n    \"name\": \"Sanchit\",\n    \"age\": \"32\",\n    \"has_kids\": false,\n    \"address\": {\n        \"p_address\": \"kalwa\",\n        \"c_addrss\": \"thane\"\n    }\n}"

