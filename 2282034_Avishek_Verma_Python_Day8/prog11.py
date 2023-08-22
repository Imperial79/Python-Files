# 11. Replace all odd numbers in numPy array with -1.
import numpy as np
b = np.array([[1, 2, 3, 4], [9, 10, 11, 12]])
b[b % 2 != 0] = -1
print(b)
