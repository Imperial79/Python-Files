'''
5. Create a list of tuples from given list of numbers, with number and its square in each tuple.
Sample Input: [2, 5, 1, 4] Output: [(2, 4), (5, 25), (1, 1), (4, 16) 
'''

lst = [2, 5, 1, 4]
lst2 = []

for i in lst:
    tup = (i, i*i)
    lst2.append(tup)

print(lst2)
