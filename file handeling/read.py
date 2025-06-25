# f = open('n1.py')
# data = f.read()
# print(data)

f = open('n1.py')
print(f.tell()) # iska use current position dekhne ke liye kiya jata hau 
data = f.read(10)
print(data)
print(f.tell())

# f = open('n1.py')
# data = f.readline()
# print(data)

# f = open('n1.py')
# data = f.readlines()
# print(type(data))
print(data)