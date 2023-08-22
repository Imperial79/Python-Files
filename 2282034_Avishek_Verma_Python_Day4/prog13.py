'''
13. Sort a list of words first by their length, largest to smallest, and then alphabetically to break ties
among words of the same length (using sorted() and lambda).
Sample Input: ['mtech', 'btech', 'mca', 'bca', 'diploma', 'dsc']
Output: ['diploma', 'btech', 'mtech', 'bca', 'dsc', 'mca']

'''
lst = ['mtech', 'btech', 'mca', 'bca', 'diploma', 'dsc']


def cust_key(str):
    return -len(str), str.lower()


print('Sorted using sorted()',sorted(lst, key=cust_key))

lst2 = ['mtech', 'btech', 'mca', 'bca', 'diploma', 'dsc']

print('Sorted using lambda', sorted(lst2, key=lambda x: (-len(x), x)))
