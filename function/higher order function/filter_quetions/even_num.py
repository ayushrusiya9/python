def even(n):
    return n % 2 == 0

num = [1,2,3,4,5,6,7,8,9]

result = list(filter(even, num))

print(result)