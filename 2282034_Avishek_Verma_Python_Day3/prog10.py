'''
10. Use a dictionary to count the frequency of letters in an input string. Only letters should be counted,
not blank spaces, numbers, or punctuation. Upper case should be considered the same as lower case.
Sample Input: This is a sentence.
Output: {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
'''

line = input('Enter a line: ').lower().split()
d = {}
for i in line:
    d[i] = d.get(i, 0) + 1

print(d)
