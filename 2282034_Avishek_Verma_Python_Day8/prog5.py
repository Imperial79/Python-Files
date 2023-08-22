# 5. Find the most frequent value in a NumPy array.
import numpy as np
a = np.random.randint(0,12,10)
print("Original Array -> ", a)
d = np.bincount(a)
print('Frequent element =>',d.argmax())