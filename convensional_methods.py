l = [10,2,4,6,8,20]#arrange this in acending order]

for i in range(len(l)-1):
    if l[i] > l[i + 1]:
        l[i],l[i + 1] = l[i + 1],l[i]
# l.sort()
print(l)
# l.reverse()

for i in range(len(l)):
    for j in range(len(l) - i - 1):
        if l[i] > l[i + 1]:
            l[i],l[i + 1] = l[i + 1],l[i]

print(l)
