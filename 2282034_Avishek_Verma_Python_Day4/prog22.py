'''
22. Write a program to obtain the line number in which a given word is present.
'''
f = open('prog22.txt', 'w')
f.write('This is 1st line in a file\n')
f.write('This is 2nd line in a file\n')
f.write('This is 3rd line in a file\n')
f.close()

f = open('prog21.txt', 'r')
txt = f.read()

word = input('Enter a word to search: ')

txt = txt.split('\n')
isFound = False
for i in range(len(txt)):
    if word in txt[i]:
        isFound = True
        print('Your word was found in line', i+1)

if not isFound:
    print(word, 'was not found in any of the lines')
