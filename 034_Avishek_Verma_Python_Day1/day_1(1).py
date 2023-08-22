# 1. i) Write a script that reads two integers, and prints the average of the two numbers.
# ii) Modify 1.i) to print the larger of the two numbers.

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print('Average of {} & {} is {}'.format(a, b, (a+b)/2))

if (a > b):
    print('{} is greater than {}'.format(a, b))
else:
    print('{} is greater than {}'.format(b, a))
