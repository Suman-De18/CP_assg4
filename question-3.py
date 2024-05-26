import numpy as np
import time

# LCG parameters
a = 10203
c = 11234567
m = 2**32
seed = 1  # Arbitrary seed

def lcg(n, seed, a, c, m):
    numbers = np.zeros(n)
    numbers[0] = seed
    for i in range(1, n):
        numbers[i] = (a * numbers[i-1] + c) % m
    return numbers / m

# Measure time for LCG method
start_time1 = time.time()
lcg_random_numbers = lcg(10000, seed, a, c, m)
lcg_time = time.time() - start_time1

print(f"Time taken by LCG method: {lcg_time:.10f} seconds")

# Measure time for np.random.rand method
start_time2 = time.time()
numpy_random_numbers = np.random.rand(10000)
numpy_time = time.time() - start_time2

print(f"Time taken by np.random.rand() method: {numpy_time:.10f} seconds")
