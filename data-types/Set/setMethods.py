#add,update,remove,discard ye importnt hai
s = {10,23,32,'python','php'}
s.add('juj')
print(s)
s.update('php','go')
# s.update(10,20)
s.update([12,32])
# print(s.pop())
# s.remove(11)#error ai hai 11 ma
s.discard(90)

s1 = s.copy()
print(s)
print(id(s))
print(s1)
print(id(s1))

s.clear()
print(s) 

#verible ya dtayp ma set ko set() aise krege to empty set aise krenge