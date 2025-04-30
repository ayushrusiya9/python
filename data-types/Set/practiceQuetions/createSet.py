#. Create a set named `colors` that contains the values 'red', 'green', 'blue'. 

# color = {'red', 'green', 'blue'}
# print(color)

#2. What will be the output of this? 
#    s = set([1, 2, 2, 3, 4, 4]) 
#    print(s) 

s = set([1, 2, 2, 3, 4, 4])
print(s)
print(type(s))

#3.. Create an empty set and verify its type. 

se = set()
print(type(se))

#4.. Explain the difference between remove() and discard() methods with an example. 

new = {1,2,2,3,4,3,3}
# new.remove(2)# 2 is remove 
# new.remove(6)# now remove give error because elemnt is not exist in set and this is stop code execution
new.discard(2)# 2 is remove like remove 
new.discard(21)# but now main gam, 21 is not exist in my set but they don't give me error and not stop code execution
print(new)