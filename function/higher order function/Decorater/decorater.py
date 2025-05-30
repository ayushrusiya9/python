def outer_func():
    def inner_func(x):
        # return 'Hello from inner function.....'
        x = x + 5
        return x
    
    return inner_func

x = outer_func()
print(x)
z = x(10)
print(z)