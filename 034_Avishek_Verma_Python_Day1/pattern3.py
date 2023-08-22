# * * * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


n = int(input('Enter the rows: '))

for i in range(0, n):
    for j in range(0, n):
        if (i + j < n):
            print('* ', end='')
    print('\r')
