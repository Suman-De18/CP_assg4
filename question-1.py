import numpy as np
import matplotlib.pyplot as plt

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

# Generate 10,000 random numbers
n = 10000
random_numbers = lcg(n, seed, a, c, m)

# Plotting the histogram
plt.hist(random_numbers, bins=50, density=True, alpha=0.75, color='blue', edgecolor='black')

# Plot the uniform PDF
x = np.linspace(0, 1, 100)
uniform_pdf = np.ones_like(x)
plt.plot(x, uniform_pdf, 'r-', lw=2)

plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Histogram of LCG Random Numbers and Uniform PDF')

plt.show()
