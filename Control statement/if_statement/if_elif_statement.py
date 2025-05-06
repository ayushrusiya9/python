# n = int(input("Enter no"))
# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# c = int(input("Enter thired number : "))

a, b, c, = int(input("Enter first number : ")), int(input("Enter second number : ")), int(input("Enter thired number : "))

if a > b and a > c :
    print(f'a {a} is greater than {b}, {c}')
elif b > a and b > c :
    print(f'b {b} is greater then {a}, {c}')    
elif c > a and c > b :
    print(f'c {c} is greater then {a}, {b}')