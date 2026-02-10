# SIMILAR TO LIST COMPREHENSIONS
# GIVES A GENERATOR OBJECT INSTEAD OF AN EAGER LIST WHICH HAPPENS IN CASE OF LIST COMPREHENSION

# eg generate a list of even numbers
# Define using paranthesis!

generator_list = (i for i in range(20) if i%2==0)
print(generator_list) #OP: <generator object <genexpr> at 0x103688ba0>
print(type(generator_list)) #OP: <class 'generator'>

print(list(generator_list))

#SIMILAR DOING IN A LIST COMPREHENSION:
# DEFINED IN SQUARE BRACKET
list_compre = [i for i in range(20) if i%2==0]
print(list_compre) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] (EAGER LIST)
print(type(list_compre)) # <class 'list'>

# CONVERT GENERATOR TO LIST OR TUPLE
list1=list((i for i in range(20) if i%2==0))
print(list1) #OP: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
tuple1=tuple((i for i in range(20) if i%2==0))
print(tuple1) #OP: (0, 2, 4, 6, 8, 10, 12, 14, 16, 18)
