'''
3. Define a function called nums() that has three parameters, the first, an integer, is required, the second parameter mult_int is optional with a default value of 10, the final parameter switch, is also optional with a default value of False. The function should multiply the two integers together, and if switch is True, should change the sign of the product before returning it.
'''


def nums(n, mult_int=10, switch=False):
    if (switch):
        return -(n*mult_int)
    return n*mult_int


print(nums(n=10))

print(nums(n=10, mult_int=12))

print(nums(n=10, mult_int=12, switch=True))
