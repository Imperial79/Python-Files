'''
24. Write a program to accept string/sentences from the user till the user enters “END”. Save the data in a text file and then display only those sentences which begin with ‘T’.
'''

print('Enter string/sentence (type END to stop): ')
stri = []
while (True):
    a = input()
    if (a.lower() != 'end'):
        stri.append(a)
    else:
        break

f = open('prog24.txt', 'w')
f.write('\n'.join(stri))
f.close()

f = open('prog24.txt', 'r')
txt = f.read().split('\n')
for i in txt:
    if i.startswith('T'):
        print(i)
