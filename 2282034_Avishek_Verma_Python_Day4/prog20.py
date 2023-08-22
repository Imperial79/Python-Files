'''
20. Write a recursive function to find the greatest common divisor (gcd) of two integers.
'''


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(gcd(a, b))
