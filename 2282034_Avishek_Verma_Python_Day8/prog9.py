# 9. Replace negative values with zeroes in a NumPy array.
import numpy as np
b = np.array([[-1, -2, -3, 4], [9, 10, 11, 12]])
b[b < 0] = 0
print(b)
