# 1. Create a 4 x 4 NumPy array with random values and find the minimum and maximum values.

import numpy as np
a = np.random.randint(0, 100, 16)
print(a)
b = sorted(a.ravel())  # returns flattened array
print(b)
print("Minimum Value:", b[0])
print("Maximum Value:", b[-1])
