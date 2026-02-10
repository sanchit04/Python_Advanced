# Parameters : are the variables defined as inputs to the function
# Arguments : are the variables passed to the parameters of the function

def foo(a,b,c): # a,b,c are parameters here
    pass

foo(1,2,3) #1,2,3 are arguments here

# TYPES of ARGUMENTS:
# Position Argument and Keyword Argument

# Order matters in position arguments
# Order does not matter in keyword arguments

foo(c=1,b=2,a=3)

# DEFAULT AND TYPES PARAMETERS
def foo(a:int,b,c=2):
    pass
# you can assign the datatype to parameters to allow specific datatype only as a argument
# when a default value is assigned then automatically datatype restriction will be data type of defaul
# here default value is set for parameter c ,
# default parameters can only be set at last
# if rest of the other params are not having any default setup

# *args , **kwargs
# *args -> are used for positional arguments identified as tuples
# **kwargs -> are used for keyword arguments identified as dicts

def foo1(a,*args,**kwargs):
    pass

# BELOW ARE VALID WAYS:
foo1(1)
foo1(1,2)
foo1(a=1,b=3,c=2)
foo1(b=2,c=2,a=1)
foo1(1,34,5,5,6,c=10)

# ENFORCE KEYWORD ARGUMENTS:
def foo_temp(*args,last_key):
    pass

#foo_temp(1,2,3) # IT missing the keyword argument
foo_temp(1,2,4,last_key=4)

# UNPACKING ARGUMENTS FROM LIST
list1=[1,2,3]

def foo_temp1(a,b,c):
    pass

foo(*list1) # works -> a=1, b=2 , c=3 (lenght of list must match number of parameters in function)

# UNPACING ARGUMENS FROM DICT
dict1={"a":1,"b":3,"c":4}
foo(**dict1) # works -> dict key name must match with the function parameter name
