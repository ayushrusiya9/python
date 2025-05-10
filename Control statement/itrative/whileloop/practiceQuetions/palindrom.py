# palindrom using string

n = input("enter number: ")
new = "".join(reversed(n))

if n == new :
    print(f'Given {n} is palindrom.')
else :
    print(f'Given {n} is not palindrom.') 

# if n == n[::-1] :
#     print(f'Given {n} is palindrom.')
# else :
#     print(f'Given {n} is not palindrom.')    


# n = int(input("Enter number: "))

# x = n
# a = 0 
# while n > 0:
#     last_digit = n % 10
#     a = a * 10 + last_digit
#     n = n//10

# if a == x :
#     print(f'Given {x} is palindrom')    
# else:
#     print(f'Given {x} is not palindrom')
