import numpy as np
import matplotlib.pyplot as plt

random_numbers = np.random.rand(10000)

# Plotting the histogram
plt.hist(random_numbers, bins=50, density=True, alpha=0.75, color='blue', edgecolor='black')

# Plot the uniform PDF
x = np.linspace(0, 1, 100)
uniform_pdf = np.ones_like(x)
plt.plot(x, uniform_pdf, 'r-', lw=2)

plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Histogram of np.random.rand() Numbers and Uniform PDF')

plt.show()
