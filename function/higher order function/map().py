#map(function, iterable) -> sytex
def add5(n):
    return n + 5

def add5(n,m):
    # return n + m
    return n ** m

l = [1,2,3,4,5]
l1 = [1,2,3,4,5]

x = map(add5,l,l1)
print(x)
print(tuple(x))
# print(list(x))#yha per isliye nahi aya kyuki pehle ye sab data de chula tha