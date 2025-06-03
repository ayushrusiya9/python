# f = open('n2.txt','a')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.encoding)
# print(f.closed)

# f = open("n1.txt",'a')
f = open("n2.py",'a')
# f.write("This is python data")
# f.write('''n = int(input("enter any number: ")) \n
#         i = 0
#         while i <= n:
#         print(i)
#         i = i + 1
#         ''')
# f.write('''
# n = int(input("enter any number: "))
# i = 0
# while i <= n:
#     print(i)
#     i = i + 1
#     ''')

# f.writelines('This is python class','this is java')
l = ['This is python class\n','this is java\n']
f.writelines(l)
f.close()