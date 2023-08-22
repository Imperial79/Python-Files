'''
11. Sort a list of numbers based on their absolute values, writing your own function for calculating absolute value of a number and 
(i) using it in sorted() without lambda, 
(ii) using it in sorted() with lambda.
Sample Input: [-5, -7, 4, -2, -9]
Output: [-2, 4, -5, -7, -9]
'''


def sorted(lst):

    for i in range(len(lst)):
        for j in range(len(lst)):
            if abs(lst[i]) < abs(lst[j]):
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst


lst = [-5, -7, 4, -2, -9]

print('Sorted without using lambda', sorted(lst))

# print(sorted([abs(i) for i in lst], reverse=True))

lst2 = [-5, -7, 4, -2, -9]
lst2.sort(key=lambda x: abs(x))
print('Sorted using lambda', lst2)
