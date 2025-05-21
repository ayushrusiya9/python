def square(num):
    return num ** 2 + 2

data = [2,4,6,7,9,11]

result = list(map(square, data))

print(result)