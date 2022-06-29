"""
Author: Trevor Amestoy
Cornell University
Spring 2022

Generates a .gif showing the progressive formation of the Sierpinski triangle.

The algorithm which generates points converging to the triangle is:

Algorithm:
1. Specify three points as corners of a triangle (C1, C2, C3)
2. Randomly select one point in the triangle (P)
3. Randomly select one of the three corners (Ci).
4. Find the half-way point, Ph, between P and Ci, and draw that point.
5.  Set halfway point as the new point, P = Ph.
6. Repeat steps 3 - 5 for N points.
7. Be amazed.

"""

# Core modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random


# Sample a random point in a triangle
def point_on_triangle(pt1, pt2, pt3):
    """
    Random point on the triangle with vertices pt1, pt2 and pt3.

    Source: Mark Dickinson, via Stackoverflow
    https://stackoverflow.com/questions/47410054/generate-random-locations-within-a-triangular-domain
    """
    x, y = sorted([random.random(), random.random()])
    s, t, u = x, y - x, 1 - y
    return (s * pt1[0] + t * pt2[0] + u * pt3[0],
            s * pt1[1] + t * pt2[1] + u * pt3[1])


# Generate N points using the algorithm
def generate_triangle_data(N, A, B, C):
    """
    Parameters:
    -----------
    N: int
        The number of points to be generated.
    A, B, C: lists (2x1)
        The coordinates of the outter corners of the triangle.

    Returns:
    --------
    Output .png or .gif file is saved to folder containing the file.
    """

    corners = [A, B, C]

    # Initialize data arrays of points
    x_data = [pt[0] for pt in corners]
    y_data = [pt[1] for pt in corners]

    # Generate new points
    for i in range(N):

        # Start with a random point in the triangle
        if i == 0:
            new_point = point_on_triangle(A, B, C)
        else:
            # Store new point data
            x_data.append(new_point[0])
            y_data.append(new_point[1])

        # Choose a random corner
        new_corner = random.randint(0,2)

        # Calculate half-way point
        half_way = [0.5 * (new_point[0] + corners[new_corner][0]), 0.5 * (new_point[1] + corners[new_corner][1])]

        # Re-assign half-way as new point
        new_point = half_way


    return x_data, y_data

# Animate each new point
def animate_fractal(i):
    scatter_plot.set_offsets(np.c_[x_data[0:i], y_data[0:i]])
    if i%10 == 0:
        plot_label.set_text('Number of points: %d' % i)


if __name__ == '__main__':

    # Number of points
    N = int(input('Number of points: \n'))

    # Ask to produce PNG or Gif
    fig_type = input('Would you like a high-res PNG or time-lapse GIF?\nOptions: PNG, GIF.\n')

    # Ask the user if they want to use custom corners
    corner_specifications = input('Use unique corners or default (equilateral)?\n Options: unique or default.\n\n', )

    if corner_specifications == 'default':
        # Corners
        A = [0, 0]
        B = [1, 0]
        C = [0.5, np.sqrt(0.75)]
    else:
        # Start with default corners
        A = [0, 0]
        B = [1, 0]
        C = [0.5, np.sqrt(0.75)]

        # Change according to
        for corner in [A, B, C]:
            for coord in [0,1]:
                corner[coord] = float(input(f'Enter coordinate {coord + 1} of corner {corner}.\n Coordinates must be within x = [0,1] and y = [0,1].\n'))

    # Calculate range of triangle
    x_min, x_max = min(A[0], B[0], C[0]), max(A[0], B[0], C[0])
    y_min, y_max = min(A[1], B[1], C[1]), max(A[1], B[1], C[1])
    x_pad, y_pad = 0.05 * (x_max - x_min), 0.05 * (y_max - y_min)
    text_xloc, text_yloc = 0.1*x_max, 0.95*y_max

    # Generate points
    x_data, y_data = generate_triangle_data(N, A, B, C)


    # Initialize figure
    fig, ax = plt.subplots(figsize = (20,20))
    ax.set(xlim = (x_min - x_pad, x_max + x_pad), ylim = (y_min - y_pad, y_max + y_pad))
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)

    if fig_type == 'GIF':
        
        # Plot starting corners
        scatter_plot = ax.scatter(x_data[0], y_data[0], c = 'black', marker = '.', s = 0.1, alpha = 1)
        plot_label = ax.text(text_xloc, text_yloc, 'Number of points: %d' % 0)
        ax.set_title('The Sierpinski Triangle')

        # Specify the number of frames and animation lag; reduce for large numbers of N
        if N < 1000:
            print_frames = N
            time_interval = 10
        else:
            print_frames = np.arange(N)[::20]
            time_interval = 5

        # Generate and save animation
        animation = FuncAnimation(fig, animate_fractal, interval = time_interval, frames = print_frames, repeat = False)
        animation.save(str('Sierpinski_triangle_' + str(N) +'_points.gif'), writer = 'pillow')
        print("Done! Check your current folder for the .gif.\n")

    elif fig_type == 'PNG':
        
        # Produce and save scatter plot
        scatter_plot = ax.scatter(x_data, y_data, c = 'black', marker = ',', s = 0.05, alpha = 1)
        plot_label = ax.text(text_xloc, text_yloc, f'Number of points: {N}')
        ax.set_title('The Sierpinski Triangle')
        plt.savefig(str('Sierpinski_triangle_' +str(N) +'_points.png'), dpi = 400)
        print("Done! Check your current folder for the .png.\n")

    else:
        print('Unknown figure type. Options are only PNG or GIF.  Retry.')

