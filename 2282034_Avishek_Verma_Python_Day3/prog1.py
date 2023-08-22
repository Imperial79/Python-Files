'''
1. Given a list of tuples, each containing name, age, and profession, generate strings of English sentences as "Name is X years old and works as Y." for each one.
Sample Input: 
[('Adnan', 25, "Programmer"), ("Swati", 27, 'DBA'), ('Anand', 26, "Tester")]
Output: 
Adnan is 25 years old and works as Programmer.
Swati is 27 years old and works as DBA.
Anand is 26 years old and works as Tester
'''

lst = [('Adnan', 25, "Programmer"),
       ("Swati", 27, 'DBA'), ('Anand', 26, "Tester")]

for i in lst:
    print(i[0], "is", i[1], "years old and works as", i[2])
