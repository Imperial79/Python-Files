'''
25. The sample file student.txt contains one line for each student. The student’s name is the first thing on each line, followed by some exam scores. The number of scores might be different for each student. Using the text file student.txt write a program that prints out the names of students those have a total score more than 500.
'''

f = open('student.txt', 'w')

f.write('John 55 45 56 87 21 52 89 65\n')
f.write('Suresh 75 55 64 90 61 58 22\n')
f.write('Ramesh 25 54 89 76 95 87 56 74\n')
f.write('Jessica 78 55 86 63 54 89 75 45\n')
f.write('Jennifer 58 96 78 46 96 77 83 53\n')
f.close()


f = open('student.txt', 'r')
studLst = f.readlines()
s = 0

for i in studLst:
    i = st = i.split()
    i = [int(i[a]) for a in range(1, len(i))]
    if sum(i) > 500:
        print(st[0], 'has scored more than 500')
