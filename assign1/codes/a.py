import numpy as np
import matplotlib.pyplot as plt

# Function to calculate X(n)
def calculate_x_n(a, r, n):
    return a * (r ** n) if n >= 0 else 0

# Values for a and r
a_value = 2
r_value = 0.5

# Generate values for n
n_values = np.arange(0, 10, 1)

# Calculate X(n) for each n
x_n_values = [calculate_x_n(a_value, r_value, n) for n in n_values]

# Plotting
plt.stem(n_values, x_n_values, basefmt="b-")
plt.xlabel('n')
plt.ylabel('X(n)')
plt.title('X(n) = ar^n')
plt.savefig('figure__plot.png')
plt.show()
