#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 18:03:07 2022

@author: cristian F. Zapata
"""
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]

x_data = np.array([0, 1, 2, 3])
y_data = np.array([0, 1 / 2, 2, 3 / 2])

n = len(x_data) - 1
h = np.diff(x_data)

u = h[:-1] / (h[:-1] + h[1:])
l = 1 - u

d = np.zeros(n - 1)
for i in range(1, n - 2):
    d[i] = 3 * (
        l[i - 1] * (y_data[i + 2] - y_data[i + 1]) / h[i + 1]
        + u[i - 1] * (y_data[i + 1] - y_data[i]) / h[i]
    )

d[0] = 3 * (
    l[0] * (y_data[1] - y_data[0]) / h[0] + u[0] * (y_data[2] - y_data[1]) / h[1]
) - l[0] * (1 / 5)
d[n - 2] = (
    3
    * (
        l[n - 2] * (y_data[n - 1] - y_data[n - 2]) / h[n - 2]
        + u[n - 2] * (y_data[n] - y_data[n - 1]) / h[n - 1]
    )
    - l[n - 2] * 0.2
)

print(d)

A = np.zeros([n - 1, n - 1])
for i in range(1, n - 2):
    A[i, i - 1] = l[i - 1]
    A[i, i] = 2
    A[i, i + 1] = u[i]

A[0, 0] = A[n - 2, n - 2] = 2
A[0, 1] = u[0]
A[n - 2, n - 3] = l[n - 2]

print(A)

M0 = np.linalg.solve(A, d)
M = np.zeros(n + 1)

for i in range(1, n):
    M[i] = M0[i - 1]

M[0] = 0.8
M[n] = 0.2

print(M)

# Plotting
for i in range(n):
    x_values = np.linspace(x_data[i], x_data[i + 1], 10000)
    y_values = (
        y_data[i]
        * ((x_values - x_data[i + 1]) ** 2)
        * (h[i] + 2 * (x_values - x_data[i]))
        / (h[i] ** 3)
        + y_data[i + 1]
        * ((x_values - x_data[i]) ** 2)
        * (h[i] + 2 * (x_data[i + 1] - x_values))
        / (h[i] ** 3)
        + M[i]
        * ((x_values - x_data[i + 1]) ** 2)
        * (x_values - x_data[i])
        / (h[i] ** 2)
        + M[i + 1]
        * ((x_values - x_data[i]) ** 2)
        * (x_values - x_data[i + 1])
        / (h[i] ** 2)
    )
    plt.plot(x_values, y_values, color="red")

plt.plot(x_values, y_values, color="red", label="Cubic Spline Interpolation")
plt.plot(x_data, y_data, marker="+", mec="r", mfc="w", label="Original Data")
plt.title("Cubic Spline Interpolation for Car Door Curve")
plt.legend()
plt.show()
