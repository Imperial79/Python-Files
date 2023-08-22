
'''
10. Write a function last_char() that takes a string as input, and returns only its last character. Use this function to sort list of strings by the last character of each string, from highest to lowest.
Sample Input: ['150', '23', '781', '19', '3478', '12', '9005', '84', '9817', '96']
Output: ['19', '3478', '9817', '96', '9005', '84', '23', '12', '781', '150']

(Using Lambda)
'''

lst = ['150', '23', '781', '19', '3478', '12', '9005', '84', '9817', '96']
lst.sort(key=lambda x: x[-1], reverse=True)
print(lst)
