
sample = set()
# Sets are an unordered collection
# Serts removes duplicates and stores unique values
# Ordered Collection (such as tuple, list, dict) supports indexing
# set is an unordered list. It doesn't support indexing

#  print({'a', 'b', 'a'})
sample = {'a', 'b', 'a'}
print(sample)

# print(dir(set()))

"""
['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""
sample.add(10)
print(sample)

s1 = {1,2,3,4}
s2 = {2,4,6,8}

print(s1.difference(s2))