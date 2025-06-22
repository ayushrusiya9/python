# normal tarika 
square = []

for i in range(10):
    square.append(i**2)

print(square)

# list comprehension

square = list(map(lambda x: x**2, range(10)))
print(square)

# another way 
# square = [x**2 for x in range(10)] #this is without conditin 
square = [x**2 for x in range(10) if x % 2 == 0]
print(square)