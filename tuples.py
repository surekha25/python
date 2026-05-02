t = ()
t1 = list()

sample = ("172.10.23.23", "172.10.23.46", True, 123, 1234.56, 34534, 34564,23223)
# print(type(sample), sample)

# <class 'tuple'> ('172.10.23.23', '172.10.23.46', True, 123, 1234.56, 34534, 34564, 23223)

# tuple is imutable. Once you define tuple variable, you cannot modified the elements

# print(sample[0])
 
# sample[0] = 12 
# print(sample) ---- not changing index element

# print(sample[0:2]) # get first 2 elements
# print(sample[-1]) # get last element

env_list = ("dev", "qa", "preprod", "prod")

# print(dir(tuple))

"""
['count', 'index']
"""

sample = (1, 3, 3, 3, 8, 0, 5, 6, 10)

# print(sample.count(3), sample.count(44))

# print(sample.index(8))

# Type Casting : data type conversion

sample = ("172.10.23.23", "172.10.23.46", True, 123, 1234.56, 34534, 34564,23223)
sample_1 = list(sample)
print(type(sample_1), sample_1, sample)
sample_t = tuple(sample_1)
print(type(sample_t))







