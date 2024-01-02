#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 22:48:24 2022

@author: cristian
"""
import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return np.sin(x**2)


def trapezoidal_rule(func, a, b, trapezoids):
    """
    Approximate the definite integral of a function using the trapezoidal rule.

    Parameters:
    - func: The function to integrate.
    - a: The lower limit of integration.
    - b: The upper limit of integration.
    - trapezoids: The number of trapezoids to use for the approximation.

    Returns:
    - area: The approximate area under the curve.
    """
    h = (b - a) / trapezoids
    xi = np.linspace(a, b, trapezoids + 1)
    fi = func(xi)
    area = h * (np.sum(fi) - 0.5 * (fi[0] + fi[-1]))
    return area


# Integration parameters
a = 0
b = np.pi / 2
trapezoids = 6

# Calculate the integral using the trapezoidal rule
approximate_area = trapezoidal_rule(func, a, b, trapezoids)

# Display the result
print("Number of trapezoids:", trapezoids)
print("Approximate Integral:", approximate_area)

# Plotting
x_values = np.linspace(a, b, 100)
y_values = func(x_values)

plt.plot(x_values, y_values, label="f(x)")
plt.fill_between(
    np.linspace(a, b, trapezoids + 1),
    0,
    func(np.linspace(a, b, trapezoids + 1)),
    color="red",
    alpha=0.3,
    label="Trapezoids",
)
plt.scatter(
    np.linspace(a, b, trapezoids + 1),
    func(np.linspace(a, b, trapezoids + 1)),
    color="red",
    marker="o",
)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Integral: Trapezoidal Rule")
plt.legend()
plt.show()
