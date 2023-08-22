import numpy as np

# 4. Create a 2d array with 1 on the border and 0 inside.
a = np.ones((5, 5), int)
a[1:-1, 1:-1] = 0
print(a)
