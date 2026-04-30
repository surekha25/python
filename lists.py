servers = ["172.10.23.23", "172.10.23.46", True, 123, 1234.56, 34534, 34564,23223]
user1 = "surekha"
user2 = "rushika"
print(servers, type(servers), user1, user2)

server_1 = servers[0]
print("server 1 IP Address", server_1)

# slicing (start_index:end_index + 1), end_index is not inclusive in python
simple_slice = servers[0:2]
print(simple_slice)

# step size (start_index:end_index + 1:step_size), end_index is not inclusive in python
step_size = servers[0:6:2]
print(step_size)

step_size = servers[1:6:2]
print(step_size)