import random

def estimate_pi(n):
    inside_circle = 0

    for _ in range(n):
        x = random.random()  # random float between 0 and 1
        y = random.random()  # random float between 0 and 1

        # Check if the point (x, y) is inside the quarter-circle
        if x*2 + y*2 <= 1:
            inside_circle += 1

    # Calculate pi approximation
    pi_estimate = 4 * (inside_circle / n)
    return pi_estimate

# Run with a large number of points
n_points = 1000000  # You can increase this for better accuracy
pi_value = estimate_pi(n_points)
print("Estimated value of pi:", pi_value)