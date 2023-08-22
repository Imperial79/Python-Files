'''
6. Extract unique values from a dictionary
'''
d = {'a': [1, 2, 3, 4], 'b': [2, 3, 4, 5]}

print("Original dictionary is ", d)
lst = list(d.values())
a = []
for i in lst:
    a += i
print(set(a))
