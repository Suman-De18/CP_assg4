import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sqrt(2/np.pi) * np.exp(-x**2 / 2)

def proposal_distribution():
    return np.abs(np.random.randn())

M = np.sqrt(2/np.pi)

def rejection_sampling(n):
    samples = []
    while len(samples) < n:
        x = proposal_distribution()
        u = np.random.rand()
        if u < f(x) / (M * np.exp(-x**2 / 2)):
            samples.append(x)
    return np.array(samples)

# Generate 10,000 random numbers using the rejection sampling method
n = 10000
random_numbers = rejection_sampling(n)

# Plotting the histogram
plt.hist(random_numbers, bins=50, density=True, alpha=0.75, color='blue', edgecolor='black')

x = np.linspace(0, np.max(random_numbers), 1000)
target_pdf = f(x)
plt.plot(x, target_pdf, 'r-', lw=2)
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Histogram of Rejection Sampling Random Numbers and Target PDF')

plt.show()
