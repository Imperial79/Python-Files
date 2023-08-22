import copy

#lst = [43,9,1,90,3,4,89]
#lst = [1,2,3,4,5,6]
lst = [9,7,6,5,4]
lst2 = copy.deepcopy(lst)
lst3 = copy.deepcopy(lst)

lst.sort()
lst3.sort(reverse = True)
if lst2 == lst:
    print("List was ascending originally")

elif lst2 == lst3:
    print("List was descernding")
else:
    print("List was unordered")