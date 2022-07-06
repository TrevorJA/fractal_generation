# fractal_generation
Contains scripts for generating and visualizing fractals. This library is meant to be a fun exploration of algorithmic fractal generation and visualization.
_Expected to be under continual, sporadic development_.

## Contents
### Sierpinski Triangle

<p align="center">
    <img src="https://github.com/TrevorJA/fractal_generation/blob/master/Sierpinski_triangle_30000_points.gif" alt = "Example animated gif of the Sierpinski triangle being plotted with 30,000 points." />
</p>

fractal_triangle_main.py
> Generates a [Sierpinski Triangle](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle). The user has the option to input the number of points desired within the plot, the type of figure produced (still PNG or animated GIF), and has the option to select unique corners for the triangle. The algorithm for generating the triangle follows:

1. Specify three points as corners of a triangle (C1, C2, C3)
2. Randomly select one point in the triangle (P)
3. Randomly select one of the three corners (Ci).
4. Find the half-way point, Ph, between P and Ci, and draw that point.
5.  Set halfway point as the new point, P = Ph.
6. Repeat steps 3 - 5 for N points.
7. Be amazed.
