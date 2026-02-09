from collections import defaultdict

# Return a default empty value if the key is not present in the dictionary
# eg -> dict1= defaultdict(list) -> so in this case if key is not found it will show empty list
dict1=defaultdict(list)
dict1["a"]=1
dict1["b"]=2

print(dict1) # OP : defaultdict(<class 'list'>, {'a': 1, 'b': 2})
print(dict1["c"]) # OP : []