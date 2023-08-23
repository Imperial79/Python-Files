# 4. Every character in the input string is followed by its frequency. Write a function to
# decrypt the string and find the nth character of the decrypted string. If no character exists
# at that position then return "-1". For Ex:- If the input string is "a2b3" the decrypted string
# is "aabbb".


a = 'a2b3'
b = ''
temp = 'a2'
n = 2
for i in range(len(a)):
    if (a[i].isdigit()):

        b += a[i-1]*int(a[i])

print(b)

if (len(b) >= n):
    print(b[n])
else:
    print('-1')
