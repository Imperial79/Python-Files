'''
21. Pair up consecutive elements of a given list.
Sample Input: [1, 3, 2, 5, 4]
Output: [[1, 3], [3, 2], [2, 5], [5, 4]]

'''
lst = [1, 3, 2, 5, 4]
lst = [int(i) for i in lst]
arr = []

for i in range(len(lst)-1):
    arr.append(lst[i:i+2])

print(arr)
