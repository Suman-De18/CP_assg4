import numpy as np
import matplotlib.pyplot as plt

# Load the data from the file
random_numbers = np.loadtxt('exponential_random_numbers.txt')

# Plotting the histogram
plt.hist(random_numbers, bins=50, density=True, alpha=0.75, color='blue', edgecolor='black')

# Plot the exponential PDF
x = np.linspace(0, np.max(random_numbers), 1000)
lambda_param = 2.0  # mean = 1/lambda = 0.5
exponential_pdf = lambda_param * np.exp(-lambda_param * x)
plt.plot(x, exponential_pdf, 'r-', lw=2)

# Adding labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Histogram of Exponential Random Numbers and Exponential PDF')

# Show plot
plt.show()
