# armtrom  given 

n = int(input("Enter number: "))

x = y = n
digit = 0
sum = 0

while n > 0 :
    digit = digit + 1
    n = n//10

while x > 0 :
    last_digit = x % 10
    sum = sum + last_digit ** digit
    x = x//10

if sum == y:
    print(f'Given {y} is armstrom')
else:
    print(f'Given {y} is not armstrom!')    