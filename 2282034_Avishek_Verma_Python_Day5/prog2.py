'''
2. Write a script that identifies the longest word(s) in a file and output a message that
includes the length of the longest word, along with all of the words of that length that
occurred in the file.
'''

rfile = open('test.txt', 'r')
maxLen = 0
lst = rfile.read()

lst = lst.split()
for i in range(len(lst)):
    for j in lst[i]:
        if not j.isalpha():
            lst[i] = lst[i].replace(j, '')

for i in lst:
    if maxLen < len(i):
        maxLen = len(i)
        max = i

print("MaxLength:", maxLen, " word:", max)

for i in lst:
    if (len(i) == maxLen):
        print(i, end='\n')
