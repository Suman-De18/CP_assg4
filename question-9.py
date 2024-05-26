import numpy as np
import matplotlib.pyplot as plt

def target_distribution(x):
    if 3 < x < 7:
        return 1 / (7 - 3)
    else:
        return 0

# Metropolis algorithm
def metropolis_algorithm(num_samples, initial_value, proposal_std):
    samples = []
    current_x = initial_value
    
    for _ in range(num_samples):
        # Propose a new candidate from a normal distribution centered at current_x
        proposed_x = np.random.normal(current_x, proposal_std)
        
        acceptance_ratio = target_distribution(proposed_x) / target_distribution(current_x)
        
        if acceptance_ratio >= 1 or np.random.rand() < acceptance_ratio:
            current_x = proposed_x
        
        samples.append(current_x)
    
    return np.array(samples)

# Parameters for the Metropolis algorithm
num_samples = 10000
initial_value = 5  
proposal_std = 0.5  # Standard deviation of the proposal distribution

# Generate samples using the Metropolis algorithm
samples = metropolis_algorithm(num_samples, initial_value, proposal_std)

# Plot the Markov Chain
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(samples, lw=0.5)
plt.title('Markov Chain')
plt.xlabel('Iteration')
plt.ylabel('Value')
plt.ylim(2,8)

# Plot the histogram of the samples
plt.subplot(1, 2, 2)
plt.hist(samples, bins=30, density=True, alpha=0.75, color='blue', edgecolor='black')

# Plot the true uniform distribution
x = np.linspace(3, 7, 1000)
uniform_pdf = np.ones_like(x) / (7 - 3)
plt.plot(x, uniform_pdf, 'r-', lw=2, label='Uniform PDF')

plt.title('Density Histogram and True Distribution')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()

plt.tight_layout()
plt.show()
