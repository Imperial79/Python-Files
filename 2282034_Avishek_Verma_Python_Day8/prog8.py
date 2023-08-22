# 8. Reverse a NumPy array.
import numpy as np
b = np.array([[1, 2, 3, 4], [9, 10, 11, 12]])
b = b.ravel()
print(b)
print(b[::-1])
