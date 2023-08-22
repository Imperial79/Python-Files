'''
* * * * * * *
  * * * * *
    * * *
      *
'''

n = int(input('Enter the rows: '))

for i in range(int(n/2)+1):
    for j in range(n):
        if ((i <= j) and (i+j <= n-1)):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
