'''
7. Append dictionary keys and values (in order), all keys before all values.
Sample Input: {1: "Jan", 2: "Feb", 3: "Mar"}
Output : [1, 2, 3, 'Jan', 'Feb', 'Mar']
'''

d = {1: 'jan', 2: 'Feb', 3: 'Mar'}

print(list(d.keys()) + list(d.values()))
