# 10. Extract all odd numbers from a numPy array.
import numpy as np
b = np.array([[1, 2, 3, 4], [9, 10, 11, 12]])
print(b[b % 2 != 0])
