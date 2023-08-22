'''
11. Use a dictionary to count the frequency of words in an input string. Only words should be counted,
not blank spaces, numbers, or punctuation. Upper case should be considered the same as lower case.
Sample Input: Fear leads to anger; Anger leads to hatred; Hatred leads to conflict;
 Conflict leads to suffering.
Output: {'fear': 1, 'leads': 4, 'to': 4, 'anger': 2, 'hatred': 2, 'conflict': 2, 'suffering': 1}
'''

line = input('Enter a line: ').lower().split()
d = {}
for word in line:
    for charac in word:
        if not (charac.isalpha()):
            word = word.replace(charac, '')
    d[word] = d.get(word, 0) + 1

print(d)
