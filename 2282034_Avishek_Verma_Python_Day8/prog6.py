# 6. Interchange two axes of a NumPy array.
import numpy as np
a = np.array([[1, 2, 3, 4], [9, 10, 11, 12]])
b = np.swapaxes(a, 0, 1)
print(b)
