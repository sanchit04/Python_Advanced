list_original = [1,2,3,4,5,6,"abc"]

list_copy = list_original
# When we use an assignment operator it does not creates a
# true copy for list which is a mutable object
# It will just create a reference to list_original


list_copy.insert(3,"Hello i am added in copy")
list_original.append("hello")

# Thus when we insert something into list_copy or even into list_original
# both list_copy and list_original will be updated/modified
print("with = operator copy:",list_copy)
print("with = operator original:",list_original)

#OP:
# with = operator: [1, 2, 3, 'Hello i am added in copy', 4, 5, 6, 'abc', 'hello']
# with = operator: [1, 2, 3, 'Hello i am added in copy', 4, 5, 6, 'abc', 'hello']

# TO Eliminate this effect and have true copy
# we should either use list() function or list slicing [:] to create a new copy
# OR SHALLOW COPY Can be leveraged here

list_copy = list(list_original)
list_copy.append("I am added in the copy list by list()")
print("with list() copy",list_copy)
print("with list() original",list_original)
#OP:
# with list() copy [1, 2, 3, 'Hello i am added in copy', 4, 5, 6, 'abc', 'hello', 'I am added in the copy list by list()']
# with list() original [1, 2, 3, 'Hello i am added in copy', 4, 5, 6, 'abc', 'hello']

list_copy = list_original[:]
list_copy.append("I am added in the copy list by [:]")
print("with list[:] copy",list_copy)
print("with list[:] original",list_original)
#OP:
# with list[:] copy [1, 2, 3, 'Hello i am added in copy', 4, 5, 6, 'abc', 'hello', 'I am added in the copy list by [:]']
# with list[:] original [1, 2, 3, 'Hello i am added in copy', 4, 5, 6, 'abc', 'hello']

import copy

list_copy = copy.copy(list_original)
list_copy.append("I am added in the copy list by shallow copy")
print("with list shallow copy copy",list_copy)
print("with list shallow copy original",list_original)
#OP:
# with list shallow copy copy [1, 2, 3, 'Hello i am added in copy', 4, 5, 6, 'abc', 'hello', 'I am added in the copy list by shallow copy']
# with list shallow copy original [1, 2, 3, 'Hello i am added in copy', 4, 5, 6, 'abc', 'hello']