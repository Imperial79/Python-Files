'''
15. Given a dictionary with grocery items and their price, update the dictionary with an added item of total price of all of the groceries in the dictionary.
Sample input ->
{"apples": 100.50,"bananas": 40, "oranges": 150, "bread": 12.50, "milk": 23.50, "eggs": 39}
Sample output ->
{'apples': 100.5, 'bananas': 40, 'oranges': 150, 'bread': 12.5, 'milk': 23.5, 'eggs': 39, 'total': 365.5}
'''

d = {"apples": 100.50, "bananas": 40, "oranges": 150,
     "bread": 12.50, "milk": 23.50, "eggs": 39}

print('Original dictionary ->', d)
d.setdefault('total', sum(list(d.values())))
print('After Sum -> ', d)
