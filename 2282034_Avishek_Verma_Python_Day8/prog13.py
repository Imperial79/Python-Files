# 13. Use NumPy to randomly generate an array with 250 values, where the mean is 120, and the standard deviation is 12. Use Matplotlib to create a histogram on that generated data.

import numpy as np
import matplotlib.pyplot as plt

a = np.random.normal(loc=120, scale=12, size=250)
# print('Mean = ', np.mean(a))
# print(a)
plt.hist(a)
plt.show()
