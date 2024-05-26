import numpy as np
import matplotlib.pyplot as plt

def box_muller(n):
    u1 = np.random.rand(n // 2)
    u2 = np.random.rand(n // 2)
    
    # Apply the Box-Muller transform
    r = np.sqrt(-2 * np.log(u1))
    theta = 2 * np.pi * u2
    z0 = r * np.cos(theta)
    z1 = r * np.sin(theta)
    
    # Combine the pairs into a single array
    return np.concatenate((z0, z1))

# Generate 10,000 Gaussian-distributed random numbers
n = 10000
random_numbers = box_muller(n)

# Plotting the histogram
plt.hist(random_numbers, bins=50, density=True, alpha=0.75, color='blue', edgecolor='black')

# Plot the Gaussian PDF
x = np.linspace(-4, 4, 1000)
gaussian_pdf = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)
plt.plot(x, gaussian_pdf, 'r-', lw=2)
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Histogram of Box-Muller Random Numbers and Gaussian PDF')

plt.show()
