import json

emp = '{"name":"ayush", "age":"20","course":"b.tech"}'
print('type of emp', type(emp))

print("Conver json to python")

d = json.loads(emp) # save in d

d = json.loads(emp) # save in d
print(f"d = {d} type of d = {type(d)}")