import numpy as np

# Function to check if a point is inside the 10-dimensional unit sphere
def is_inside_sphere(point):
    return np.sum(point**2) <= 1

# Monte Carlo integration to estimate the volume of a 10-dimensional unit sphere
def monte_carlo_integration(num_samples, dimensions=10):
    inside_sphere = 0

    for _ in range(num_samples):
        point = np.random.uniform(-1, 1, dimensions)
        if is_inside_sphere(point):
            inside_sphere += 1
    volume_hypercube = 2**dimensions
    volume_sphere = (inside_sphere / num_samples) * volume_hypercube
    return volume_sphere

num_samples = 1000000

estimated_volume = monte_carlo_integration(num_samples)

print(f"Estimated volume of the 10-dimensional unit sphere: {estimated_volume}")
