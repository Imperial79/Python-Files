'''
23. Write a program to read the given CSV file student_marks.csv having tab delimiter.
'''


f = open('student_marks.csv', 'r')
txt = f.read()

print(txt.replace(',', '\t'))
