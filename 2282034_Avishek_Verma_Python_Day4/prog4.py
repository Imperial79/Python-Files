'''
4. Write a function add_mult() that will accept two numbers and calculate the result of addition and multiplication of them and return both results in a single return statement.
'''


def add_mult(a, b):
    return {'add': a+b, 'mul': a*b}


res = add_mult(10, 7)
print('Addition', res['add'], ', Multiplication:', res['mul'])
