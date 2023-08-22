
lst = [1,2,3,4,5,6]

lst[0], lst[len(lst)-1] = lst[len(lst)-1], lst[0]

print(lst)
