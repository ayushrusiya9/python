def to_upper(word):
    return word.upper()

fruits = ['apple','mango','kiwi']

result = list(map(to_upper, fruits))
print(result)