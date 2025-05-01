# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}

# print(s1.union(s2))

# print(s1.intersection(s2))

# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))

#intesection update 

# s1.intersection_update(s2)
# s2.intersection_update(s1)
# print(s1)
# print(s2)

#difference update

# s1.difference_update(s2)
# print(s1)



# print(s1.isdisjoint(s2))#False
# print(s1.issubset(s2))#False
# print(s1.issuperset(s2))#False

s1 = {1,2,3,4}
s2 = {1,2,3,4}
print(s1.issuperset(s2))
print(s1.issubset(s2))