'''
1. Write a program which can iterate through a list of users (tuples comprising of a name, email, and age) and if the user is at least 18 years old, adds her/him to a dictionary. Write an exception hierarchy which defines a different exception for each of these error conditions:

• the name is not unique
• the age is not a positive integer
• the user is under 18
• the email format is not valid

Raise these exceptions where appropriate. Whenever an exception occurs, your program
should move onto the next set of data in the list. Print different error messages for each
different kind of exception.
'''

import re

tup = (("Avishek", 'avishekverma79@gmail.com', 22),
       ("Akash", 'akash@gmail.com', 18),
       ("Vivek", 'vivek@gmail.com', 10))
d = dict()
k = 1
name = []
for i in range(len(tup)):

    try:
        if tup[i][0] in name:
            name.append(tup[i][0])
            raise Exception('Duplicate Name')
        elif tup[i][2] < 0:
            raise Exception('Age should pe positive')
        elif tup[i][2] < 18:
            raise Exception('Age is under 18')
        elif re.search("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", tup[i][1]) == None:
            raise Exception("Email is not valid")
        else:
            d.setdefault(k, tup[i])
            k += 1
    except Exception as e:
        print(tup[i][0], e)
        continue

print(d)
