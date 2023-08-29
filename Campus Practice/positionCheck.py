q = [2, 5, 1, 3, 4]
q = [1, 2, 5, 3, 7, 8, 6, 4]
s = 0
for pos in range(len(q)):
    if (q[pos] > pos+1):
        s += q[pos]-(pos+1)
    if (q[pos] > (pos+1) and q[pos] - (pos+1) > 2):
        s = "Too chaotic"
        break
print(s)
