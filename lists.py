l1 = []
l1 = list()

servers = ["172.10.23.23", "172.10.23.46", True, 123, 1234.56, 34534, 34564,23223]
user1 = "surekha"
user2 = "rushika"
print(servers, type(servers), user1, user2)

server_1 = servers[0]
print("server 1 IP Address", server_1)

# slicing (start_index:end_index + 1), end_index is not inclusive in python
simple_slice = servers[0:2]
print(simple_slice)

print(servers)
simple_slice = servers[1:]
print(simple_slice)
simple_slice = servers[:5]
print(simple_slice)
simple_slice = servers[:]
print(simple_slice)
# step size (start_index:end_index + 1:step_size), end_index is not inclusive in python
step_size = servers[0:6:2]
print(step_size)

step_size = servers[1:6:2]
print(step_size)

simple_slice = servers[-1:-4:-1]
print(simple_slice)

print("lenght of list", len(simple_slice))

# List is mutable datatype
# Mutable:  once defined, can change at any time Eg - List, dictonaries
# Immutable: Once defined, can't be changed Eg - Tuple, sets

print("Before Modify", servers)
servers[-3] = 12345678
print("After Modification:", servers)

print("List of Operations:", dir(servers))

""" 
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
 """
servers.append(["a", "b"])
print("last", servers)
print(servers[-1][0])
print("After Append", servers, len(servers))
servers.extend(["c", "d"])
print("After Extend", servers, len(servers))
print(servers.index(True))
servers.insert(0, 12)
print(servers)
servers.remove(12)
print(servers)
servers.reverse()
print(servers)
servers = servers[::-1]
print(servers)

servers = [1, 5, 7, 9, 2, 14]
# servers.sort()
servers_1 = sorted(servers)
print(servers, servers_1)

servers = ["172.10.23.23", "172.10.23.46", True, 123, 1234.56, 34534, 34564,23223]
servers_1 = servers.copy()
servers_1.remove(123)
print(servers, servers_1) 

"""
Important Topics 

1. Reverse a list
2. Sort vs Sorted
3. Integer division vs Floor division
4. Shallow Copy (inplace operation not happend in original data)
5. Multi Indexing
6. Append vs Extend
7. Mutable vs Immutable
8. dir()
"""