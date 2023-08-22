'''
6. sin(x) can be calculated approximately by summing the terms of the infinite series as follows
sin(x) = x - x**3/3! + x**5/5! - x**7/7! …
where x is expressed in radians. Write function(s) to calculate the value of sin x, accepting x as degree from user. Compare your results with that of math.sin().
'''

import math


def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


def sinx(x, n):
    s = 0
    a = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            s -= (x**a)/fact(a)
        else:
            s += (x**a)/fact(a)
        a += 2
    return s


print("Sinx Calculated by sinx(): ", sinx(2, 4))
print("Sinx calculated by math.sin(): ", math.sin(2))
