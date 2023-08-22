'''
2. Write a function attached() that takes three parameters, the first a required parameter that is a number, the second a required parameter that is a string, and the third an optional parameter whose default is “ ”. Returned value will be the first parameter, concatenated with the second, using the third.
'''


def attached(num, st, op=" "):
    return (str(num) + op + st)


print(attached(num=10, st='Avishek'))
