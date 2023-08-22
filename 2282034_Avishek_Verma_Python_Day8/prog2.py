# 2. Create a random vector of size 10 and sort it.
import numpy as np
vec = np.random.randint(0, 100, 10)
print("Original vector ->", vec)
vec = sorted(vec.ravel())
print("Sorted vector ->", vec)
