import sys

x = 10
print(sys.getsizeof(x))


x = ''
print(sys.getsizeof(x))

import sys

x = ()
print(sys.getsizeof(x))

import sys

x = {}
print(sys.getsizeof(x))

import sys

x = []
print(sys.getsizeof(x))

# import sys

# x = set()
# print(sys.getsizeof(x))