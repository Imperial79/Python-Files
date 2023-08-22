# 2. Write a script that reads three floating point numbers, and does the following:
# i) It prints the smallest and largest among the three.
# ii) It prints the average of the three numbers up to 2 decimal places


a = float(input('Enter 1st float number: '))
b = float(input('Enter 2nd float number: '))
c = float(input('Enter 3rd float number: '))

if (a > b and a > c):
    print('{} is largest'.format(a))
elif (b > c):
    print('{} is largest'.format(b))
else:
    print('{} is largest'.format(c))

avg = (a+b+c)/3

print('Average of ({}, {}, {}) = {}'.format(a, b, c, round(avg, 2)))
