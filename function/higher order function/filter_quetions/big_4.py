def is_big(word):
    return len(word) > 4

words = ['apple','elephant','kiwi']

result = list(filter(is_big, words))

print(result)