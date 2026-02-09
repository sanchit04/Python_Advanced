from collections import OrderedDict

# ordered dict is a type of dict which can preserve the order in which keys are added to the dict
# this has became less important since 3.7 normal dict also supports preserved ordering
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict ['b'] = 2
ordered_dict ['c'] = 3

print(ordered_dict) #OP : OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Since we are using python 3.9 ordering of dict is supported in normal dict.
normal_dict = dict(a=1,b=2,c=3)
print(normal_dict) #OP : {'a': 1, 'b': 2, 'c': 3}