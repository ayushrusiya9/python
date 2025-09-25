# Lambda function likh:
# Jo number ko triple kare
# Jo string ko reverse kare
# Jo do number me se bada return kare

triple =  lambda a,b: (a*3, b*3)

result = triple(3,3)

print(result)

reverse = lambda s: s[::-1]

print(reverse("ayush"))

# bigNum = lambda a,b: (a,b)[a > b]
bigNum = lambda a,b: a if a > b else b

res = bigNum(5,9)

print(res)