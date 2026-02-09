# INFINITE ITERATORS count,cycle,repeat

#count
from itertools import count,cycle,repeat

#It will start from 10 and go on till we break it !
# at this point we are breaking at 15
for i in count(10):
    if i==15:
        break
    print(i)
#OP:
# 10
# 11
# 12
# 13
# 14
# 15

# cycle
# it will print in a cyclic manner the input which we give to it it will do infinitely unless break
a=["hello","word","how r you"]
counter=0
for i in cycle(a):
    counter+=1
    if counter==10:
        break
    print(i)

#OP:
# hello
# word
# how r you
# hello
# word
# how r you
# hello
# word
# how r you

# repeat
# infinite time give value is repeated
for i in repeat("hello",10):
    # in this case hello will be repeated 10 times, if 10 was not givcn it will do infinite
    print(i)

#OP:
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
