'''
14. Given a dictionary, which contains group names with the list of users (Users can belong to multiple
groups), create a dictionary with the users as keys and a list of their groups as values.
Sample input
{"local":["admin", "Ananya"],"public":["admin", "Zahir"], "administrator":["admin"] }
Sample output
{'admin': ['local', 'public', 'administrator'], 'Ananya': ['local'], 'Zahir': ['public']}
'''

d = {"local":["admin", "Ananya"],
     "public":["admin", "Zahir"], 
     "administrator":["admin"] }
lst= {}
for k in d:
     for v in d[k]:
          if(v not in lst):
               lst[v] = [k]
          else:
               lst[v].append(k)
print(lst)         




