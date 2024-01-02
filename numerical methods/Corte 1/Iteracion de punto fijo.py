# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 20:40:08 2022

@author: Cristian F. Zapata

"""
import numpy as np
import matplotlib.pyplot as plt

# Function Definition
f = lambda x: (3 + x - 2 * x**2) ** (1 / 4)


# Iteration of Fixed Point
def fixed_point_iteration(func, initial_guess, iterations, tolerance):
    prev_iteration = initial_guess
    table = []

    for i in range(iterations):
        current_iteration = func(prev_iteration)
        error = abs((current_iteration - prev_iteration) / current_iteration) * 100

        table.append([i + 1, current_iteration, func(current_iteration), error])

        if error <= tolerance:
            break

        prev_iteration = current_iteration

    return table


# Plotting Function
def plot_fixed_point_iteration(table):
    xi = table[:, 1]
    yi = table[:, 2]

    order = np.argsort(xi)
    xi = xi[order]
    yi = yi[order]

    plt.plot(xi, yi, "o-")
    plt.axhline(0, color="black")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Fixed Point Iteration on f(x)")
    plt.grid()
    plt.show()


# Main Execution
if __name__ == "__main__":
    # Fixed Point Iteration parameters
    initial_guess = 1
    iterations = 100
    tolerance = 0.000001

    # Execute Fixed Point Iteration method
    result_table = fixed_point_iteration(f, initial_guess, iterations, tolerance)

    # Print the result table
    np.set_printoptions(precision=4)
    print("[i, itr_act, evalu, error]")
    print(np.array(result_table))

    # Plot the Fixed Point Iteration process
    plot_fixed_point_iteration(np.array(result_table))
