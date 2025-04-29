#1.copy() -> create copy new object
#2. clear() -> remove all pair from dictionary
#3.pop() -> remeove targeted key from dict
#3. popitem() -> remove last element from dict
#4. get('key) -> return value from targeted key
#5. keys() -> 
# 6. values() 
#7. items() -
#8. fromkeys()



# d = {"name":"ayush", "age": 20, "course": "b.tech"}

# d2 = d.copy()
# print(d)
# print(d2)
# print(id(d))
# print(id(d2))
# d2.clear()
# print(d2)
# del d2
# # print(d2)


# d = {"name":"ayush", "age": 20, "course": "b.tech"}

# d.pop("age")
# print(d)
# print(id(d))


# d = {"name":"ayush", "age": 20, "course": "b.tech"}

# d.popitem()
# print(d)


# d = {"name":"ayush", "age": 20, "course": "b.tech"}
# # new = d.get('name')

# print(d.get('name'))
# print(d)


# d = {"name":"ayush", "age": 20, "course": "b.tech"}

# # d.keys()
# print(d.keys())

# d = {"name":"ayush", "age": 20, "course": "b.tech"}

# print(d.values())


# s = [10,2,34]
# # s = "python"
# # s = [1,2,3,4,5,'python']

# d = dict.fromkeys(s,10)

# print(d)

# d = {'x':10, 'y':20, 'z':30}

# d.setdefault('x',50)
# print(d)

# d.setdefault('p',50)
# print(d)

# d1 = {'q': 2, 'r': 3}
# d.update(d1)
# print(d)
# print(d1)

d = {}
d['name'] = 'ayush'
print(d)
d['name'] = 'asshu'

x = d['name']
print(x)
print(type(d))