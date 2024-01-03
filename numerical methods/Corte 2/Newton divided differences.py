#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:42:00 2022

@author: cristian F. Zapata
"""

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INPUT, Test data
xi = np.array([3, 5, 7, 9])
fi = np.array([-1, -3, 9, 6])

# PROCEDURE

# Divided Differences Table Initialization
title = ["i   ", "xi  ", "fi  "]
n = len(xi)
ki = np.arange(0, n, 1)
table = np.concatenate(([ki], [xi], [fi]), axis=0)
table = np.transpose(table)

# Initialize an empty divided differences array
divided_diff_array = np.zeros(shape=(n, n), dtype=float)
table = np.concatenate((table, divided_diff_array), axis=1)

# Calculate the divided differences table, starting from column 3
[n, m] = np.shape(table)
diagonal = n - 1
j = 3
while j < m:
    # Add title for each column
    title.append("F[" + str(j - 2) + "]")

    # Calculate each cell in the column
    i = 0
    step = j - 2
    while i < diagonal:
        denominator = xi[i + step] - xi[i]
        numerator = table[i + 1, j - 1] - table[i, j - 1]
        table[i, j] = numerator / denominator
        i = i + 1
    diagonal = diagonal - 1
    j = j + 1

# POLYNOMIAL with Divided Differences
divided_diff_first_row = table[0, 3:]
n = len(divided_diff_first_row)

# Polynomial expression using Sympy
x = sym.Symbol("x")
polynomial = fi[0]
for j in range(1, n, 1):
    factor = divided_diff_first_row[j - 1]
    term = 1
    for k in range(0, j, 1):
        term = term * (x - xi[k])
    polynomial = polynomial + term * factor

# Simplify the polynomial
polynomial_simplified = polynomial.expand()

# Polynomial for numerical evaluation
px = sym.lambdify(x, polynomial_simplified)

# Puntos para la gráfica
muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a, b, muestras)
pfi = px(pxi)

# OUTPUT
np.set_printoptions(precision=4)
print("****************************************************************************")
print("Divided Differences Table")
print([title])
print(table)
print("****************************************************************************")
print("Divided Differences: ")
print(divided_diff_first_row)
print("****************************************************************************")
print("Polynomial: ")
print(polynomial)
print("****************************************************************************")
print("Simplified Polynomial: ")
print(polynomial_simplified)
print("****************************************************************************")

# Plotting
plt.plot(xi, fi, "o", label="Data Points")
for i in range(0, n, 1):
    plt.axvline(xi[i], ls="--", color="r")
plt.plot(pxi, pfi, label="Polynomial")
plt.legend()
plt.xlabel("xi")
plt.ylabel("fi")
plt.title("Newton Divided Differences Polynomial")
plt.show()
