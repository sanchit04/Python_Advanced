#NAMED TUPLE
# similar to structs, easy to create light weight object type.

from collections import namedtuple

#Creates a class by Name Point which has 3 instance attributes x,y,z
Point = namedtuple('Point','x,y,z')
pt=Point(x=1,y=2,z=3)
print(pt) #OP -> Point(x=1, y=2, z=3)
print(type(pt)) # <class '__main__.Point'>
print(pt.x) # OP : 1