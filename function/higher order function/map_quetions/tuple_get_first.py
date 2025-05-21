def get_first(t):
    return t[0]

items = [(1,2),(3,4),(5,6)]

result = list(map(get_first, items))

print(result)