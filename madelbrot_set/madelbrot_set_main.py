"""
Trevor Amestoy
Cornell University
Spring 2022

Plotting the Mandlebrot set

Source:
https://realpython.com/mandelbrot-set-python/
"""

# Core modules
import numpy as np
import matplotlib.pyplot as plt


# Ignore overflow warning
np.warnings.filterwarnings('ignore')

# Initialize candidate values
def complex_matrix(xmin, xmax, ymin, ymax, density):
    real = np.linspace(xmin, xmax, int((xmax-xmin) * density))
    imaginary = np.linspace(ymin, ymax, int((ymax - ymin) * density))
    return real[np.newaxis, :] + imaginary[:, np.newaxis] * 1j


# Check if candidate values are within bound <= 2
def is_stable(c, n_iterations):
    z = 0
    for _ in range(n_iterations):
        z = z **2 + c
    return abs(z) <= 30


# Select only those numbers in the mandelbrot set
def filter_set_members(c, n_iterations):
    mask = is_stable(c, n_iterations)
    return c[mask]


# Generate low-res scatter plot
c = complex_matrix(-2, 0.5, -1.5, 1.5, density = 100)
mandelbrot_numbers = filter_set_members(c, n_iterations = 30)

plt.scatter(mandelbrot_numbers.real, mandelbrot_numbers.imag, color = 'black', marker = ',', s = 1)
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()

