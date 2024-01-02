# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:05:23 2022

@author: Cristian F. Zapata
"""

import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol
from scipy.misc import derivative

# Newton-Raphson for multiple roots

f = lambda x: np.exp(-x) + x - 2


def nrmultiple(f, c0, itr, tolerance):
    x0 = c0
    table = []

    for i in range(itr):
        d1f = derivative(f, x0, dx=1e-10, n=1)
        d2f = derivative(f, x0, dx=1e-10, n=2)

        x1 = x0 - ((d1f * f(x0)) / (((d1f) ** 2) - f(x0) * d2f))
        evaluation = f(x1)
        error = abs((x1 - x0) / x1) * 100

        table.append([i + 1, x1, evaluation, error])

        if error <= tolerance:
            break

        x0 = x1

    return table


table = nrmultiple(f, 1, 4, 0.0001)
table = np.array(table)

# TABLE
np.set_printoptions(precision=3)
print("[i+1, x1, function evaluated, error]")
print(table)

xi = table[:, 1]
yi = table[:, 2]

# Sort points for the graph
order = np.argsort(xi)
xi = xi[order]
yi = yi[order]

plt.plot(xi, yi)
plt.plot(xi, yi, "o")
plt.axhline(0, color="black")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Newton-Raphson for multiple roots of f(x)")
plt.grid()
plt.show()
