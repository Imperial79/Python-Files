'''
19. Write a recursive function to get the sum of digits of a non-negative integer. 
'''


def recur(n):
    if n == 0:
        return 0
    else:
        return n % 10 + recur(n//10)


print(recur(35))
