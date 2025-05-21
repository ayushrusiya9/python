def add_gst(price):
    return round(price * 1.18, 2)

prices = [199, 249, 399]

result = list(map(add_gst, prices))

print(result)