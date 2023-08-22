'''
9. Write a function last_char() that takes a string as input, and returns only its last character. Use this function to sort list of strings by the last character of each string, from highest to lowest.
Sample Input: ['150', '23', '781', '19', '3478', '12', '9005', '84', '9817', '96']
Output: ['19', '3478', '9817', '96', '9005', '84', '23', '12', '781', '150']
'''


def last_char(line):
    return line[-1]


lst = ['150', '23', '781', '19', '3478', '12', '9005', '84', '9817', '96']

arr = []
for i in range(len(lst)):
    for j in range(len(lst)):
        if last_char(lst[i]) > last_char(lst[j]):
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
print(lst)
