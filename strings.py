sample = "Hello, how are you doing"

# print(dir(sample))

"""
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""

print(sample.casefold())
print(sample.center(60,"#"))

# Reverse String
print(sample[::-1])

sample_1 = "abc"
print(tuple(sample_1), list(sample_1))

sample = "Hello, how are you doing"

print(sample.split(" "))
print("#".join(sample.split(" ")))

# concatenation :  joining 2 strings
print("a" + "#" + "b") # a#b

# how do you print a file path
print(r"C:\devops\daws-86s\repos\python\strings.py")
