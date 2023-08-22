'''
18. Write a recursive function to get the list sum.
[Test Data: [1, 2, [3,4], [5,6]] , Expected Result: 21] 
'''


def recur(lst):
    sum = 0
    for i in lst:
        print(type(i))

        if type(i) == type([]):
            sum += recur(i)
        else:
            sum += i
    return sum


print(recur([1, 2, [3, 4], [5, 6]]))
