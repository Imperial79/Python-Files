'''
7. Write a function that accepts a list and returns a new list with unique elements of the first list. 
'''


def uniLst(lst):

    return list(set(lst))


print(uniLst([1, 1, 1, 2, 3, 2, 3, 8]))
