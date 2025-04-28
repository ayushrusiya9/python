t = (1,2,3,'python')
print(type(t))
print(id(t))

#methods of tuple
#1. len()
t = (1,2,3,'python')
print(len(t))

#2. max()
# t = (1,2,3,'python')
t = (1,2,3,4,5)
print(max(t))

#3.min()
# t = (1,2,3,'python')
t = (1,2,3,4,5)
print(min(t))

#4. sum()
# t = (1,2,3,'python')
# t = ('python','java','php')
t = (1,2,3,4,5)
print(sum(t))


#tuple have only 2 methods
#1. index()

t = (1,2,3,4,"python")
print(t.index(3))

#2. count()
t = (1,2,3,4,"python")
print(t.count("jva"))


#getsizeof 
import sys

l = [1,2,3]
tu = (1,2,3)
print(sys.getsizeof(l))
print(sys.getsizeof(t))

#tuple is fast as comapare to list 