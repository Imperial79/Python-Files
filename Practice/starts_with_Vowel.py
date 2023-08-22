#Print words starts with vowel in a string

lineList = input('Enter a line: ').split(' ')
vowel = ['a', 'e', 'i', 'o', 'u']

for i in lineList:
    if(i[0].lower() in vowel):
        print(i)


