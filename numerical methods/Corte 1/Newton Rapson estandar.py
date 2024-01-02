# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 17:47:01 2022

@author: Cristian F. Zapata

"""
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from scipy.misc import derivative

# Newton-Raphson Standard Method

x = sp.Symbol("x")
f = lambda x: np.exp(-x) + x - 2


def nr_standard(f, initial_guess, iterations, tolerance):
    current_iteration = initial_guess
    table = []

    for i in range(iterations):
        fx_evaluated = f(current_iteration)
        fdx_evaluated = derivative(f, current_iteration, dx=1e-10)

        if fdx_evaluated == 0:
            print("The derivative is zero.")
            break
        else:
            next_iteration = current_iteration - (fx_evaluated / fdx_evaluated)

        function_evaluated = f(next_iteration)
        error = abs((next_iteration - current_iteration) / next_iteration) * 100

        current_iteration = next_iteration
        table.append(
            [i + 1, next_iteration, current_iteration, function_evaluated, error]
        )

        if error <= tolerance:
            break

    return table


# Main Execution
if __name__ == "__main__":
    # Execute Newton-Raphson Standard Method
    result_table = nr_standard(f, 1, 4, 0.000001)

    # Print the result table
    np.set_printoptions(precision=3)
    print("[i+1, itr_act, itr_ant, funcion_evalu, error]")
    print(np.array(result_table))

    # Plot the Newton-Raphson Standard Method process
    xi = np.array(result_table)[:, 1]
    yi = np.array(result_table)[:, 3]

    order = np.argsort(xi)
    xi = xi[order]
    yi = yi[order]

    plt.plot(xi, yi, "o-")
    plt.axhline(0, color="black")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Newton-Raphson Standard Method on f(x)")
    plt.grid()
    plt.show()
