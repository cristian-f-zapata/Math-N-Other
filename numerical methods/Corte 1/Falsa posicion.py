# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 19:35:52 2022

@author: Cristian F. Zapata

"""
import numpy as np
import matplotlib.pyplot as plt

# Function Definition
f = lambda x: x**2 - 0.7


# Regula Falsi Method
def regula_falsi_method(func, lower_limit, upper_limit, iterations, tolerance):
    prev_iteration = 0
    table = []

    for i in range(iterations):
        if func(upper_limit) - func(lower_limit) == 0:
            print(
                "Cannot divide by zero: f({}) - f({}) = 0".format(
                    func(upper_limit), func(lower_limit)
                )
            )
            break

        current_iteration = upper_limit + (
            func(upper_limit)
            * (lower_limit - upper_limit)
            / (func(upper_limit) - func(lower_limit))
        )
        evaluated = func(current_iteration)
        error = abs((current_iteration - prev_iteration) / current_iteration) * 100

        table.append(
            [i + 1, current_iteration, upper_limit, lower_limit, evaluated, error]
        )

        if error <= tolerance:
            break

        if func(lower_limit) * func(current_iteration) < 0:
            upper_limit = current_iteration
        else:
            lower_limit = current_iteration

        if func(lower_limit) * func(current_iteration) == 0:
            print("Root found earlier than expected.")
            break

        prev_iteration = current_iteration

    return table


# Plotting Function
def plot_regula_falsi(table):
    xi = table[:, 1]
    yi = table[:, 4]

    order = np.argsort(xi)
    xi = xi[order]
    yi = yi[order]

    plt.plot(xi, yi, "o-")
    plt.axhline(0, color="black")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Regula Falsi on f(x)")
    plt.grid()
    plt.show()


# Main Execution
if __name__ == "__main__":
    # Regula Falsi parameters
    lower_limit = 0.5
    upper_limit = 2
    iterations = 3
    tolerance = 0.0000001

    # Execute Regula Falsi method
    result_table = regula_falsi_method(
        f, lower_limit, upper_limit, iterations, tolerance
    )

    # Print the result table
    np.set_printoptions(precision=3)
    print("[i, itr_act, sup, inf, evaluada, error ]")
    print(np.array(result_table))

    # Plot the Regula Falsi process
    plot_regula_falsi(np.array(result_table))
