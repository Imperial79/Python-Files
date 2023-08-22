'''
21. Write a program to find number of characters, words, spaces and lines in a file.
'''

f = open('prog21.txt', 'w')
f.write('This is 1st line in a file\n')
f.write('This is 2nd line in a file\n')
f.write('This is 3rd line in a file\n')
f.close()

f = open('prog21.txt', 'r')
txt = f.read()

ch = sp = words = lines = 0
for i in txt:
    ch += 1
    if i == '\n':
        lines += 1

print('Characters->', ch)
print('Lines->', lines)
print('spaces->', txt.count(' '))
print('Words->', len(txt.split()))
