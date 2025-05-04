# fs = frozenset({1,2,3})
# fs1 = frozenset({3,4,5})

fs = frozenset("abc")
fs1 = frozenset("bcd")

print(fs.difference(fs1))