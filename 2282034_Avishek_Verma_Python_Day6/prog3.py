'''
3. import re and write scripts to achieve the following:
(i) accept a mobile number as input, and if it starts with 00, replace the 00 with 91
(ii) takes a word as input and satisfy the requirements that it should be of 5 letters,
starts with ‘c’ and ends with ‘r’
(iii) assume a product cataloging system has the following requirements:
 - first symbol: an uppercase character
 - second symbol: a digit
 - third symbol: the special character @
 - fourth symbol: a lowercase character
write a script that accepts an id and checks whether it is in correct format or not
(iv) check whether a given mail id is in valid format or not.
'''

import re

mob = input('Enter Mobile No: ')
x = re.search("^00", mob)
if x != None:
    print('91'+mob[2:])

line = input('Enter a line: ')
x = re.search("^c.*r$", line)
if x != None and len(line) == 5:
    print('Valid String')
else:
    print('Invalid String')


id = input('Enter an ID: ')
x = re.search("^[A-Z][0-9][@][a-z]$", id)
if x != None:
    print('Valid ID')
else:
    print('Invalid ID')


email = input('Enter email: ')
x = re.search(
    "^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", email)

if x != None:
    print('Valid E-Mail')
else:
    print('InValid E-Mail')
