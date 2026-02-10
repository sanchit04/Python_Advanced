# CALL BY OBJECT CONCEPT

def foo(num):
    num=4

my_num=10
print(my_num) #OP : 10
foo(my_num)
print(my_num) #OP : 10

# my_num does not changes since int is an immutable object
# But when it comes to list

def foo(list1):
    list1.append(10)

my_list=[1,2,3]
print(my_list) # OP: [1, 2, 3]
foo(my_list)
print(my_list) # OP: [1, 2, 3, 10]

# REBINDING CASE :
# IN this case it did not change as list1 was rebinded in the function
def foo(list1):
    list1=[1,2,3]
    list1.append(10)

my_list=[1,2,3]
print(my_list) # OP: [1, 2, 3]
foo(my_list)
print(my_list) # OP: [1, 2, 3]

# ONE MORE CASE:
# in this case as well a new list object was created without hampering the original argument object

def foo(list1):
    list1=list1+[200,300,400]
my_list=[1,2,3]
print(my_list) # OP: [1, 2, 3]
foo(my_list)
print(my_list) # OP: [1, 2, 3]

# WHERE IT WILL MODIFY?
# += will update existing!
def foo(list1):
    list1+=[200,300,400]
my_list=[1,2,3]
print(my_list) # OP: [1, 2, 3]
foo(my_list)
print(my_list) # OP: [1, 2, 3, 200, 300, 400]



