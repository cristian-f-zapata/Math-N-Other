#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 16:41:58 2022

@author: cristian F. Zapata
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Lagrange Interpolation


def lagrange_interpolation(xi, fi):
    n = len(xi)
    x = sym.Symbol("x")
    polynomial = 0
    divisor_L = np.zeros(n, dtype=float)

    for i in range(n):
        numerator = 1
        denominator = 1
        for j in range(n):
            if j != i:
                numerator *= x - xi[j]
                denominator *= xi[i] - xi[j]
        term_Li = numerator / denominator

        polynomial += term_Li * fi[i]
        divisor_L[i] = denominator

    simplified_polynomial = polynomial.expand()
    interpolation_function = sym.lambdify(x, simplified_polynomial)
    return simplified_polynomial, divisor_L, interpolation_function


# Given data
xi_values = [2, 2.75, 4]
fi_values = [1 / 2, 1 / 2.75, 1 / 4]  # Replace with your function values

# Lagrange Interpolation
(
    lagrange_polynomial,
    divisor_L,
    lagrange_interpolation_function,
) = lagrange_interpolation(xi_values, fi_values)

# Display results
print("****************************************************************************")
print("Given function values (fi):", fi_values)
print("Denominators in L(i):", divisor_L)
print("****************************************************************************")
print("Complete Lagrange Polynomial:")
print(lagrange_polynomial)
print("****************************************************************************")
print("Simplified Lagrange Polynomial:")
print(lagrange_polynomial)
print("****************************************************************************")

# Plotting
x_values = np.linspace(np.min(xi_values), np.max(xi_values), 101)
y_values = lagrange_interpolation_function(x_values)

plt.plot(xi_values, fi_values, "o", label="Data Points")
plt.plot(x_values, y_values, label="Interpolation Polynomial")
plt.legend()
plt.xlabel("xi")
plt.ylabel("fi")
plt.title("Lagrange Interpolation of f(x)")
plt.show()
