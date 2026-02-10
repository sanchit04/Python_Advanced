# Shallow copy : One level deep only reference of nested child object
# Deep copy: full independent copy

org_list = [1,2,3,4]
copy_list = org_list # Does not provide a true copy
copy_list.append(100)
print(org_list) # [1, 2, 3, 4, 100]
print(copy_list) # [1, 2, 3, 4, 100]

# Here to tackle this we can use shallow copy
import copy
org_list = [1,2,3,4]
copy_list = copy.copy(org_list) # Does not provide a true copy
copy_list.append(100)
print(org_list)  # [1, 2, 3, 4]
print(copy_list)  # [1, 2, 3, 4, 100]

# WHEN IN CASES of MORE COMPLEX LISTS: NESTED LISTS
org_list= [[0,1,2,3,4],[5,6,7,8]]
copy_list = copy.copy(org_list) # Shallow copy works only for one level thus we need deep copy here
copy_list[0][1]=100
print(org_list) # [[0, 100, 2, 3, 4], [5, 6, 7, 8]]
print(copy_list) # [[0, 100, 2, 3, 4], [5, 6, 7, 8]]

org_list= [[0,1,2,3,4],[5,6,7,8]]
copy_list = copy.deepcopy(org_list) # deep copy used
copy_list[0][1]=100
print(org_list) # [[0, 1, 2, 3, 4], [5, 6, 7, 8]]
print(copy_list) # [[0, 100, 2, 3, 4], [5, 6, 7, 8]]

