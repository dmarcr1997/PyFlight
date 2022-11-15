"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle
import numpy as np
from breadth_first_search import breadth_first, visualize_path

t = turtle.Turtle()

for c in ['red', 'green', 'blue', 'yellow']:
    t.color(c)
    t.forward(75)
    t.left(90)

start = []
end = []
for i in range(2):
    elm = input(f'Enter start location {i+1}: ')
    start.append(int(elm))

print(start)

for i in range(2):
    elm = input(f'Enter goal location {i+1}: ')
    end.append(int(elm))
print(end)

grid = np.array([
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
])

print(
    visualize_path(grid, breadth_first(grid, tuple(start), tuple(end)),
                   tuple(start)))
