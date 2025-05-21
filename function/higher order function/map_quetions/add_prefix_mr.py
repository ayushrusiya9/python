def add_prefix(word):
    return 'Mr. ' + word

names = ['Ayush', 'Aditya','Safdar','Ehthesham']

result = list(map(add_prefix, names))

print(result)