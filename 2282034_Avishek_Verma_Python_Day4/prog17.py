'''
17. Use lambda to sort a list of names alphabetically by last name.
Sample Input: ['Ales Bialiatski', 'Alain Aspect', 'Anton Zeilinger', 'Douglas Diamond']
Output: ['Alain Aspect', 'Ales Bialiatski', 'Douglas Diamond', 'Anton Zeilinger']
'''
lst = ['Ales Bialiatski', 'Alain Aspect', 'Anton Zeilinger', 'Douglas Diamond']

print(sorted(lst, key=lambda x: x.split(" ")[1]))
