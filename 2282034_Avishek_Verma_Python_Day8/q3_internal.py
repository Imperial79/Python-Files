import numpy as np
arr = np.random.randint(0, 100, 30)
arr = np.sort(arr)
mean = np.mean(arr)
arr[arr % 2 != 0] = mean
print(arr)
