'''
8. Write a function that accepts a comma separated string of words as input and returns a colonseparated string of words after sorting them alphabetically.
'''


def colonSeparated(line):
    return '-'.join(sorted(line.lower().replace(' ', '').split(',')))


print(colonSeparated('Avishek, Verma,is , a ,good,boy'))
