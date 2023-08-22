'''
4. Find maximum and minimum k elements in a Tuple. 
'''
new_tup = (3, 6, 1, 8, 3, 5, 0)

k = int(input("Enter the value of k: "))
lst = sorted(set(new_tup))
print(lst[:k] + lst[-k:])
