# SHALLOW COPY FOR CLASSES
import copy

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1 = Person("Sanchit",34)
#COPYING P1 to P2
p2=p1 #JUST CREATED A REFERENCE
p2.age=28
print(p1.age) # 28
print(p2.age) # 28

p1_og = Person("Sanchit",34)
p2_shallow_copy = copy.copy(p1_og)
p2_shallow_copy.age=28
print(p1_og.age) # 34
print(p2_shallow_copy.age) # 28

# DEEP COPY WITH CLASSES
import copy

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Company:
    def __init__(self,boss,employee):
        self.boss=boss
        self.employee=employee

p1 = Person("Sanchit",21)
p2 = Person("Vinod",39)

c1 = Company(p2,p1)
c2 = copy.copy(c1)

c2.boss.age=34
print(c1.boss.age) # 34
print(c2.boss.age) # 34

# Shallow copy cannot support this level nesting thus we need to use deepcopy here
p1 = Person("Sanchit",21)
p2 = Person("Vinod",39)
c1 = Company(p2,p1)
c2 = copy.deepcopy(c1)
c2.boss.age=34
print(c1.boss.age) # 39
print(c2.boss.age) # 34
