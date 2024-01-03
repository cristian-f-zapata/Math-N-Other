# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 20:58:02 2022

@author: Cristian F. Zapata


"""
import matplotlib.pyplot as plt
import numpy as np


# Bisection Function
def bisection_method(func, lower_limit, upper_limit, iterations, tolerance):
    prev_iteration = 0
    table = []

    for i in range(iterations):
        current_iteration = (lower_limit + upper_limit) / 2
        func_eval = func(current_iteration)
        error = abs((current_iteration - prev_iteration) / current_iteration) * 100
        table.append(
            [i + 1, lower_limit, current_iteration, upper_limit, func_eval, error]
        )

        if error <= tolerance:
            break

        if (func(lower_limit) * func(current_iteration)) < 0:
            upper_limit = current_iteration
        else:
            lower_limit = current_iteration

        prev_iteration = current_iteration

    return table


# Plotting Function
def plot_bisection(table):
    xi = table[:, 2]
    yi = table[:, 4]

    order = np.argsort(xi)
    xi = xi[order]
    yi = yi[order]

    plt.plot(xi, yi, "o-")
    plt.axhline(0, color="black")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Bisection on f(x)")
    plt.grid()
    plt.show()


# Main Execution
if __name__ == "__main__":
    # Define the function
    function = lambda x: np.exp(-x) + np.cos(x) - np.log(x)

    # Bisection parameters
    lower_limit = 0.5
    upper_limit = 1.5
    iterations = 5
    tolerance = 0.001

    # Execute bisection method
    result_table = bisection_method(
        function, lower_limit, upper_limit, iterations, tolerance
    )

    # Print the result table
    np.set_printoptions(precision=3)
    print("[i+1, lower_limit, current_iteration, upper_limit, f(c), error ]")
    print(np.array(result_table))

    # Plot the bisection process
    plot_bisection(np.array(result_table))
