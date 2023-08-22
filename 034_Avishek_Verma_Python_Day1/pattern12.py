
'''
* * * * * * *
* * *   * * *
* *       * *
*           *
* *       * *
* * *   * * *
* * * * * * *
'''

n = int(input('Enter the rows: '))

for i in range(n):
    for j in range(n):

        if ((i+j <= int(n/2)) or (j-i >= int(n/2)) or (i-j >= int(n/2)) or i+j >= (int(n/2) + (n-1))):
            print('* ', end='')
        else:
            print('  ', end='')
    print('\r')
