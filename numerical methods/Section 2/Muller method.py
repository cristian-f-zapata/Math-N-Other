# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 16:41:58 2022

@author: cristian F. Zapata
"""
# Muller methold

import numpy as np
import matplotlib.pyplot as plt


def muller(f, x0, x1, x2, tol, max_iter):
    i = 1
    table = []
    error = 1e3
    x3 = 0

    while error > tol:
        c = f(x2)
        b = ((x0 - x2) ** 2 * (f(x1) - f(x2)) - (x1 - x2) ** 2 * (f(x0) - f(x2))) / (
            (x0 - x2) * (x1 - x2) * (x0 - x1)
        )
        a = ((x1 - x2) * (f(x0) - f(x2)) - (x0 - x2) * (f(x1) - f(x2))) / (
            (x0 - x2) * (x1 - x2) * (x0 - x1)
        )
        x3 = x2 - (2 * c) / (b + np.sign(b) * np.sqrt(b**2 - 4 * a * c))
        error = abs(x3 - x2)
        table.append([i, x3, f(x3), error])
        x0, x1, x2 = x1, x2, x3

        if i == max_iter:
            break

        i += 1

    return table


# Example usage:
f = lambda x: np.exp(-x) - x**2 + np.sin(x)
initial_guesses = [0, 0.5, 1]
tolerance = 1e-10
max_iterations = 8

table = muller(f, *initial_guesses, tolerance, max_iterations)
table = np.array(table)

# Print the table
np.set_printoptions(precision=3)
print("[i, x3, function evaluated, error]")
print(table)

# Plot the convergence
xi = table[:, 1]
yi = table[:, 2]

order = np.argsort(xi)
xi = xi[order]
yi = yi[order]

plt.plot(xi, yi)
plt.plot(xi, yi, "o")
plt.axhline(0, color="black")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Muller's Method for f(x)")
plt.grid()
plt.show()
