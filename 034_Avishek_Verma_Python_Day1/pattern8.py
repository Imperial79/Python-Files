'''
      *
    * * *
  * * * * *
* * * * * * *
'''

n = int(input('Enter the rows: '))

for i in range(int(n/2)+1):
    for j in range(n):
        if ((i+j >= int(n/2)) and (j-i <= int(n/2))):
            print('* ', end='')
        else:
            print('  ', end='')
    print('\r')
