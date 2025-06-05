def natural(n):
    i = 1
    while i <= n:
        yield i
        i = i + 1

# n = int(input('Enter number: '))
n = 10

x = natural(n)

# for i in x:
#     print(i)
print(type(x))
print(next(x))
print("hello")

print(next(x))