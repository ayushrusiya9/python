l = [1,2,3,4,5,6,7,8,9,10]

def even_no(n):

    if n % 2 == 0:
        return n
    

x = filter(even_no, l)

# print(x)
# print(list(x))

def greater5(n):

    if n >= 5:
        return n

y = filter(greater5, l)

# print(list(y))

# without inbuit methd

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = []

for i in l1:

    if i >= 5:
        l2.append(i)

print(l2)