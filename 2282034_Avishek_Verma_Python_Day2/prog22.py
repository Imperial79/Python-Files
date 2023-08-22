'''
22. Create a list containing every possible sublist of a list.
'''

lst = [1, 2, 3]
lst = [int(i) for i in lst]
sub = [[], ]

for i in range(1, len(lst)+1):
    for j in range(len(lst)):
        if lst[j:j+i] not in sub:
            sub.append(lst[j:j+i])

print(sub)
