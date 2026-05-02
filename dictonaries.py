# dictonaries are key:value pair based
# Also known as hashmaps

d = {}
d_1 = dict()

sample = {'a':1, 'b':2}
# print(type(sample))
# print(sample['a'], sample.get('b'))

# Dictonaries are mutable datatype
sample['a'] = 10
# print(sample)

# keys in dictonaries, once defined can't be changed
# Hence they should be of immutable datatype, for ex- tuple, string

sample = {('a','b'):1, 'b':2}
# print(sample)

# print(dir(dict))

"""
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
"""

# print(sample.keys(), sample.values(), sample.items())

sample_list = [('a', 1), ('b', 2)]
# type casting
sample_dict = dict(sample_list)
print(sample_dict)