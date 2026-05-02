# dictonaries are key:value pair based
# Also known as hashmaps

d = {}
d_1 = dict()

sample = {'a':1, 'b':2}
print(type(sample))
print(sample['a'], sample.get('b'))

# Dictonaries are mutable datatype
sample['a'] = 10
print(sample)

# keys in dictonaries, once defined can't be changed
# Hence they should be of immutable datatype, for ex- tuple, string