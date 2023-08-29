
a = [1, 2, 3, 4, 3, 2, 1]


d = {}
for i in a:
    if (i in d):
        d[i] += 1
    else:
        d[i] = 1
c = 0
for i in d.values():
    c += 1
    if (i == 1):
        break

print(list(d.keys())[c-1])
