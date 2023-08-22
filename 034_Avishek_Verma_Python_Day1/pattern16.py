n = int(input('Enter n: '))

if (n % 2 == 0):
    n += 1

for i in range(n):
    for j in range(n):
        if (i+j <= (n-1) and j >= i and j >= int(n/2)) or (j <= int(n/2) and i >= j and i+j >= (n-1)):
            print(' * ', end='')
        else:
            print('   ', end='')
    print()
