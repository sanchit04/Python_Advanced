# GENERATORS gives an iterable object which is lazy in nature
# Its a normal function but with yield statement instead of return
# Generators can be consumed only once!
# We dont have to wait before we start to use them

def my_generator():
    yield 1
    yield 2
    yield 3

g=my_generator()
print(g)
print(type(g))
# for i in g:
#     print(i)

# We see a StopIteration error here since we have already consumed the generator in the FOR LOOP
# above for loop needs to be commented for this to work
# If above is not commented OP:
# Traceback (most recent call last):
#   File "/Users/sanchitgawde/PycharmProjects/PYTHON_ADVANCED/generators_ex.py", line 15, in <module>
#     value = next(g)
# StopIteration

value = next(g)
print(value) #OP 1
value=next(g)
print(value) #OP 2
value=next(g)
print(value)  #OP3
#value=next(g)
#OP: (Since theres no yield left!)
# Traceback (most recent call last):
#   File "/Users/sanchitgawde/PycharmProjects/PYTHON_ADVANCED/generators_ex.py", line 29, in <module>
#     value=next(g)
# StopIteration


#Calculate sum with generators
def my_generator_2():
    yield 4
    yield 5
    yield 6

g=my_generator_2()
print(sum(g)) # 15 -> 4+5+6 -> 15

# IMPLEMENT A COUNTDOWN with generator
def count_down(count_down_start):
    while count_down_start>=0:
        yield count_down_start
        count_down_start-=1

g=count_down(10)
for i in g:
    print(i)

#OP:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0

# IF same we had to do using list
# it wont be memory efficient and its eager as well will need to store in list first

