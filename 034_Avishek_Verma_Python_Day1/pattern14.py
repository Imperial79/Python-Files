'''
      *
      * *
      * * *
* * * * * * *
  * * *
    * *
      *
'''

n = int(input('Enter the rows: '))

for i in range(n):
    for j in range(n):

        if ((i+j >= int(n/2) and j-i <= int(n/2) and i <= int(n/2)) or (i-j <= int(n/2) and i+j <= (int(n/2) + (n-1)) and i >= int(n/2))) and ((j <= int(n/2) and i + j >= int(n/2) and i <= int(n/2)) or (j >= int(n/2) and i+j <= (int(n/2) + (n-1)) and i >= int(n/2))):
            print('* ', end='')
        else:
            print('  ', end='')
    print('\r')
