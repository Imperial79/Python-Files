import copy
'''
16. Given a dictionary that contains a student’s roll, name and a list of marks,
(i) Update the dictionary with an added item of the total of the student’s marks.
Sample Input: {"roll": 5, "Name": "Ananya", "marks": [79, 88, 92]}
Output: {'roll': 5, 'Name': 'Ananya', 'marks': [79, 88, 92], 'total': 259}
(ii) Update the dictionary with an added entry of the total of the student’s marks in the list.
Sample Input: {"roll": 5, "Name": "Ananya", "marks": [79, 88, 92]}
 Output: {'roll': 5, 'Name': 'Ananya', 'marks': [79, 88, 92, 259]}
(iii) Update the dictionary with the list replaced by the total marks of the student
Sample Input: {"roll": 5, "Name": "Ananya", "marks": [79, 88, 92]}
 Output: {'roll': 5, 'Name': 'Ananya', 'marks': 259}
'''

stud1 = {"roll": 5, "Name": "Ananya", "marks": [79, 88, 92]}
stud2 = copy.deepcopy(stud1)
stud3 = copy.deepcopy(stud1)
print('(i) Update the dictionary with an added item of the total of the student’s marks.')

stud1.setdefault('total', sum(stud1['marks']))
print(stud1)

print('(ii) Update the dictionary with an added entry of the total of the student’s marks in the list.')
stud2['marks'].append(sum(stud2['marks']))
print(stud2)

print('(iii) Update the dictionary with the list replaced by the total marks of the student')

stud3['marks'] = sum(stud3['marks'])
print(stud3)
