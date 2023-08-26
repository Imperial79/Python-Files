str1 = 'listen'
str2 = 'silent'

for i in str1:
    if (str2.__contains__(i)):
        print(i)
        str2 = str2.replace(i, '', 1)

if (len(str2) == 0):
    print("They are anagrams")
else:
    print("They are not")
