def new(**n): #as per documentattion **kwargs
    # print(n)
    # print(type(n))
    # for k,v in n.items():
    #     print(f'keys is {k} and value is {v}')

    for k in n.keys():
        print(f'keys is {k}')

    for v in n.values():
        print(f'value is {v}')

new(name="aush",age=20,quali='b.tech')