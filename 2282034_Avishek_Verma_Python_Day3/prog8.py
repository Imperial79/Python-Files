'''
8. Sort the items of a dictionary (i) by keys, (ii) by values
'''

d = {2: 'Jan', 1: 'Feb', 0: 'Mar'}

print('Sorted by keys -> ', sorted(d.items()))

d2 = {}
for i, j in sorted([(v, k) for k, v in d.items()]):
    d2[j] = i
print('Sorted by values -> ', d2)
