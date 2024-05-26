import numpy as np

# Function to check if a point is inside the unit circle
def is_inside_circle(x, y):
    return x**2 + y**2 <= 1

num_samples = 100000
# Monte Carlo integration to estimate the area of the unit circle
def monte_carlo_integration(num_samples):
    inside_circle = 0

    # Generate random points and check if they are inside the unit circle
    for _ in range(num_samples):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if is_inside_circle(x, y):
            inside_circle += 1

    # The area of the bounding square is 4 (since side length is 2)
    area_square = 4
    area_circle = (inside_circle / num_samples) * area_square
    return area_circle


estimated_area = monte_carlo_integration(num_samples)

print(f"Estimated area of the unit circle: {estimated_area}")
