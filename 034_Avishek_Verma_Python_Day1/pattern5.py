# *
# * *
# * * *
# * * * *
# * * *
# * *
# *


n = int(input('Enter the rows: '))

for i in range(n):
    for j in range(n):
        if (i+j <= n-1 and i >= j):
            print('*', end=' ')
        else:
            print('_', end=' ')

    print()
