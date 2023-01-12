"""
Author: Trevor Amestoy
Cornell University
Spring 2022

Generates a points within a sierpinski hexagon

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
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Generate N points using the algorithm
def generate_sierpinski_hexagon(N):
    """
    Parameters:
    -----------
    N: int
        The number of points to be generated.

    Returns:
    --------
    points : array
        Points within the sierpinski hexagon
    """

    # Points on the hexagon
    A = [0.0, 1.0]
    B = [0.866, 0.5]
    C = [0.866, -0.5]
    D = [0.0, -1.0]
    E = [-0.866, -0.5]
    F = [-0.866, 0.5]

    corners = [A, B, C, D, E, F]

    # Initialize data arrays of points
    x_data = [pt[0] for pt in corners]
    y_data = [pt[1] for pt in corners]

    # Generate new points
    for i in range(N):

        # Start with a random corner
        if i == 0:
            new_point = corners[random.randint(0,5)]
        else:
            # Store new point data
            x_data.append(new_point[0])
            y_data.append(new_point[1])

        # Choose a random corner
        new_corner = random.randint(0,5)

        # Calculate two-thirds distance to new point
        half_way = [(3/4)*(new_point[0] + corners[new_corner][0]),  (3/4)* (new_point[1] + corners[new_corner][1])]

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

    # Points on the hexagon
    A = [0.0, 1.0]
    B = [0.866, 0.5]
    C = [0.866, -0.5]
    D = [0.0, -1.0]
    E = [-0.866, -0.5]
    F = [-0.866, 0.5]

    # Calculate range of triangle
    x_min, x_max = E[0], B[0]
    y_min, y_max = D[1], A[1]
    x_pad, y_pad = 0.1 * (x_max - x_min), 0.1 * (y_max - y_min)
    text_xloc, text_yloc = 0.1*x_max, 0.95*y_max

    # Generate points
    x_data, y_data = generate_sierpinski_hexagon(N)


    # Initialize figure
    fig, ax = plt.subplots(figsize = (15,15))
    #ax.set(xlim = (x_min - x_pad, x_max + x_pad), ylim = (y_min - y_pad, y_max + y_pad))
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)

    if fig_type == 'GIF':

        # Plot starting corners
        scatter_plot = ax.scatter(x_data[0], y_data[0], c = 'black', marker = '.', s = 0.1, alpha = 1)
        plot_label = ax.text(text_xloc, text_yloc, 'Number of points: %d' % 0)
        ax.set_title('The Sierpinski Hexagon')

        # Specify the number of frames and animation lag; reduce for large numbers of N
        if N < 1000:
            print_frames = N
            time_interval = 10
        else:
            print_frames = np.arange(N)[::20]
            time_interval = 5

        # Generate and save animation
        animation = FuncAnimation(fig, animate_fractal, interval = time_interval, frames = print_frames, repeat = False)
        animation.save(str('Sierpinski_hexagon_' + str(N) +'_points.gif'), writer = 'pillow')
        print("Done! Check your current folder for the .gif.\n")

    elif fig_type == 'PNG':

        # Produce and save scatter plot
        scatter_plot = ax.scatter(x_data, y_data, c = 'black', marker = ',', s = 0.05, alpha = 1)
        plot_label = ax.text(text_xloc, text_yloc, f'Number of points: {N}')
        ax.set_title('The Sierpinski Hexagon')
        plt.savefig(str('Sierpinski_hexagon_' +str(N) +'_points.png'), dpi = 400)
        print("Done! Check your current folder for the .png.\n")

    else:
        print('Unknown figure type. Options are only PNG or GIF.  Retry.')
