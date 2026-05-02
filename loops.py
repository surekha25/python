# while loop can be used when we know when to end
# for loop can be used when we don't know when to end

# value = 0

# while value < 10:
#     if value==5:
         # Increment is very important
#         value = value + 1
#         continue
#     print(value)
#     value = value + 1

sample= ["server1", "server2", "server3", "server4"]

# idx = 0

# while idx < len(sample):
#     print(sample[idx])
#     idx += 1 # idx = idx + 1

# in -> membership operator (checks whether that element is present or not)
# print(1 in sample)
# print("server1" in sample)
      
# idx -> iterable
# sample -> iterator
# for idx in sample:
#     print(idx)
# print(idx)

# access elements inside a list with index using for loop
# range, enumerate
# print(list(range(5)))

for idx in range(len(sample)):
    ele = sample[idx]
    print(idx, ele)

for val in enumerate(sample):
    print(val)

# tuple unpacking
a, b = (1, 2)
print(a, b)

for idx,val in enumerate(sample):
    print(idx, val)