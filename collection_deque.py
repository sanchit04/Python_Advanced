# DEQUE : used to add or remove elements from queue from both end

from collections import deque

d=deque()
# .append() will add elements to right
d.append(1)
d.append(2)
print(d) #OP : deque([1, 2])

# .appendleft() will add elements to left
d.appendleft(3)
d.appendleft(4)
print(d) #OP : deque([4, 3, 1, 2])

# .pop() will remove last element from right
d.pop()
print(d) #OP:  deque([4, 3, 1])

#.popleft() will remove last element from left
d.popleft()
print(d) #OP : deque([3, 1])

#.clear use to remove all elements from deque
d.clear()
print(d) #OP: deque([])

# .extend used to adding multiple elements to deque,
# it takes an iterable object like : list,tuple,string
# adds all elements to right
d.extend([1,2,3,4])
print(d) #OP : deque([1, 2, 3, 4])

#.extendleft will add elements to left
d.extendleft([10,9,8])
print(d) #OP : IMPORTANT: deque([8, 9, 10, 1, 2, 3, 4]) ->
# here 10 is added first then to the left of 10, 9 is added
# then to the left of 9, 8 is added

#.rotate(1) will rotate one place to the right for all elements
# INITIAL: deque([8, 9, 10, 1, 2, 3, 4])
d.rotate(1)
print(d) #OP : deque([4, 8, 9, 10, 1, 2, 3])

d.rotate(2)
#will rotate by 2 elements
print(d) #OP : deque([2, 3, 4, 8, 9, 10, 1])

d.rotate(-1)
# will rotate one element to left side
print(d) #OP: deque([3, 4, 8, 9, 10, 1, 2])

