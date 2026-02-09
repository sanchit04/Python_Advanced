# TUPLE SLICING: (Same like LIST SLICING) -> TUPLE SLICING WILL RESULT IN A LIST
tuple1=([1,2,3,4,5,6,7,8,9,10])
print(tuple1[:-4:-1]) # OP -> [10,9,8] -> -1(start):-4(end):(-1)
# -> -4+1 => 3 -> -1(start):-3(end) -> 10,9,8

# when we do negative  step start if start is <no value>: it will start at last index
print(tuple1[:4:-1]) #OP-> [] -> 9(start):4+1 => 5 -> 9(start):5(end) -> [10,9,8,6]

print(tuple1[5:4:1]) #OP -> [] -> cant go back if step is positive then start should be less than end

print(tuple1[5:6:1]) #OP -> [6] -> 5 start: 6-1=5 end -> 5:5 -> [6]

print(tuple1[-10:-9:1]) #OP -> [1] -> -10 start: -9-1 -> -10 -> -10:-10 -> [1]

print(tuple1[-10:-11:1]) #OP -> [] -> cant go back if step is positive and if start and stop is negative
# then start should be greater than end

print(tuple1[-10:-11:-1]) #OP -> [1] -> -10 start: -11+1 -> -10 -> -10:-10 -> [1]

print(tuple1[-10:7:-1]) #OP -> [] -> Two different start stop will result in empty

print(tuple1[-6:-8:-1]) #OP -> [5,4] -> -8+1 = -7 end -> -6 start: -7 end

print(tuple1[-6:-8:1])  #OP -> [] -> positive step mean move right
# in negative indexing is it possible to move from -6 to -8 in right dierection NOT POSSIBLE thus its empty

# UNPACKING OF TUPLES:
# we can assign each element of a tuple to a variable directly
# THIS WORKS ONLY WHEN number of elements and number of variables match
# eg 3 elements from tuple will need 3 variable for UNPACKING
a,b,c = tuple([1,2,4])

print(a) # OP : 1
print(b) # OP : 2
print(c) # OP : 3

#TUPLE1 has many more elements that just 2 variables
#a,b = tuple1 #OP -> ValueError: too many values to unpack (expected 2)

# UNPACKING TUPLES with asterik:

a, *b = tuple1
print(a) #OP : 1 -> first element
print(b) #OP : [2, 3, 4, 5, 6, 7, 8, 9, 10] -> Returns a list of all remainder elements

a, *b, c = tuple1
print(a) #OP: 1 -> first element
print(b) #OP : [2,3,4,5,6,7,8,9] -> list of middle elements
print(c) #OP: 10 -> last element

# TUPLES are more memory effecient than list

import sys
list1=[1,"Helloworld",2,3,4]
tuple1=(1,"Helloworld",2,3,4)
print(sys.getsizeof(list1),"bytes") #OP : 120 bytes
print(sys.getsizeof(tuple1),"bytes") #OP : 80 bytes