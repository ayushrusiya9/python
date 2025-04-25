s = "i love python"
print(s.index('e'))#o/p = 5
#print(s.index('e',6))#error
#print(s.index('e',6,12))#error
#print(s.index('e',2,5))#error = ye rule ko follw krega positive -1
print(s.index('e',2,6))#5
s = "python"
x = len(s)

print(s[x-1])
