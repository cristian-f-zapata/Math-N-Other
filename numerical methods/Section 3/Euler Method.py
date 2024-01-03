# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:34:53 2022

@author: cristian F. Zapata
"""
import numpy as np
import matplotlib.pyplot as plt


def euler_method(f, a, b, h, y0):
    x_values = []
    y_values = []
    num_intervals = int((b - a) / h)
    current_x = a

    for _ in range(num_intervals):
        x_values.append(current_x)
        y_values.append(y0)
        y_next = y0 + f(current_x) * h
        y0 = y_next
        current_x += h

    return x_values, y_values


f = lambda x: np.cos(2 * x) + np.sin(3 * x)

xi, yi = euler_method(f, 0, 1, 0.25, 1)

plt.plot(xi, yi)
plt.plot(xi, yi, "o")
plt.axhline(0, color="black")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Euler Method")
plt.grid()
plt.show()

print(xi, yi)
