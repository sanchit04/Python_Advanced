
# Generating list with asterik operator
list1 = [0] * 5
print(list1) # OP -> [0, 0, 0, 0, 0]

# Concatenate two list together (Using + operator)
list2=[1,2,3,4,5]
list3 = list2 + list1

print(list3) # OP -> [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]

# SLICING
# it always creates a new list it wont affect the existing list
# creates same list like list3 (creates a new list-> IMPORTANT)
list_new=list3[:]
print(list_new)

# SLICING SYNTAX [START INDEX:END INDEX:STEP (By default 1)]
# If we give index which is more than what is available
# in list it will print till end and will not fail
list3=[1, 2, 3, 4, 5, 0, 1, 0, 2, 0]
list_test = list3[4:11]
print(list_test) #OP -> [5, 0, 1, 0, 2, 0]

# Slicing with step index
list_test=list3[4:11:2]
print(list_test) #OP -> [5, 1, 2]

# Slicing one more eg:
print(list3[4:4]) #OP -> [] , because end-1 -> 3rd index 4th to 3rd index is not possible thus its empty

print(list3[4:7]) #OP -> end-1 -> 7-1 -> 6. -> 4,6 -> [5, 0, 1]

#NEGATIVE INDEXING

# REVERSE LIST WITHOUT USING reverse method

#-1 step index means start at right most
list_test=list3[::-1]
print(list_test) #OP -> [0, 2, 0, 1, 0, 5, 4, 3, 2, 1]

list3=[1, 2, 3, 4, 5, 0, 1, 0, 2, 0]
print(list3[:4:-1]) # OP -> [0, 2, 0, 1, 0]

print(list3[2:6:-1]) # OP -> [] , because in a negative step start cannot be less than end

print(list3[6:2:-1]) # OP -> [1, 0, 5, 4] -> Start at 6 stop at end+1 (since negative) -> 6,3
