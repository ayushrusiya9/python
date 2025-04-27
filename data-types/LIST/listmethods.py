# list methods
#1. append() -> add single element in last position
#2. extend() -> add multiple element in last position
#3. insert() -> add element targeted position
#4. pop()    -> remove last element from list
#5. remove() -> remove targeted element from the list
#6. copy() -> create new object with same element
#7. clear() -> remove all element from list
#8. reverse() ->reverse all element from list
#9. sort()  -> arrange assending ordeer 
#10. index() -> find out element position
#11. count() -> calculate from occurance of any element
l = [1,2,3,4,9]
l.append(1)
# print(l)

# l.extend(20,30)
# print(l)

t = [1,2,3]
l.extend(t)
print(l)

s = 'python'
l.extend(s)
print(l)

m = [2,2,3,4,5,4,6,7,8]
m.insert(0,'python')
m.insert(1,['python','java','php'])
m.insert(19,1200)
print(m)

#pop()
p = [1,2,3,4,5,6]
print(p.pop())
print(p)
print(p.pop(0))
print(p)

#remove()
r = [1,2,3,4,5,6,7]
r.remove(3)
print(r)

#index()
i = [1,2,3,4,5,2]
# print(i.index(1))
# print(i.index(1,2))
#count()
print(i.count(20))#check element kitni baar a rha hai

#reverse 
re = ['java','python',1,2,3,4]
print(re.reverse())
print(re)

#sort()
# s = ['java','python',1,2,3,4]
s = ['python','java','php']
s.sort()
# s.reverse()
s.sort(reverse=True)
print(s)
 

#copy
co = [2,3,4,6,7,"python"]
co2 = co.copy()
print(id(co),id(co2))


#clear()
co.clear()
print(co)

del co
print(co)