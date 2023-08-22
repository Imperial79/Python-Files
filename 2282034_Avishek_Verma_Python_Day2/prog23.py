'''
23. Accept a single word, and then convert the word to Pig Latin.
[ Pig Latin: When a word begins with a consonant (such as dog) or a consonant cluster (such as
brush), take the consonant/consonant cluster and move it to the end of the word, adding the
suffix ‘ay’ to the end of the word. E.g ‘dog’ in Pig Latin becomes ‘ogday’ ; ‘brush’, becomes
‘ushbray’]
But if the first letter is a vowel, it is kept as it is and “hay” is appended to the end. Example, ‘
‘apple’ becomes ‘applehay’ ]
'''


word = input("Enter a word: ")
vowels = ['a', 'e', 'i', 'o', 'u']
arr = []
for i in word:
    if (i not in vowels):
        arr.append(i)
    else:
        break
if (len(arr) > 0):
    print(word[len(arr):] + ''.join(arr) + 'ay')
else:
    print(word + 'hay')
