arr = [4, 3, 4, 4, 2, 4]

d = {4: 1}

for i in arr:
    if d.get(i) == None:
        d[i] = 1
    else:
        d[i] += 1

print(len(d)-1)
