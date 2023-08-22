# 12. Create a four dimensions array with random values and get the sum over the last two axes.
import numpy as np
b = np.arange(72)
b = b.reshape(4, 3, 2, 3)  # multiplying these will result 72
# 4 elements represents 4-Dimensional array

print(b[..., -1:] + b[..., -2:])
