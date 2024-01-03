#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 12:25:02 2023

@author: cristian F. Zapata
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative


class NumericalMethods:
    pass

    def __init__(self, f, tolerance):
        self.f = f
        self.tolerance = tolerance


class Roots(NumericalMethods):
    def bisection(self, f, lower_limit, upper_limit, iterations, tolerance):
        previous_iteration = 0
        self.table = []

        for i in range(iterations):
            current_iteration = (lower_limit + upper_limit) / 2
            function_evaluated = f(current_iteration)
            error = (
                abs((current_iteration - previous_iteration) / current_iteration) * 100
            )
            self.table.append(
                [
                    i + 1,
                    current_iteration,
                    function_evaluated,
                    lower_limit,
                    upper_limit,
                    error,
                ]
            )

            if error <= tolerance:
                break

            if f(lower_limit) * f(current_iteration) < 0:
                upper_limit = current_iteration
            else:
                lower_limit = current_iteration

            previous_iteration = current_iteration

        table = np.array(self.table)

        np.set_printoptions(precision=3)
        print("[i+1, itr_act, f(c), lim_inf,  lim_sup,  error ]")
        print(table)

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
        plt.title("Bisection f(c)")
        plt.grid()
        plt.show()

    def newton_raphson_multiple(self, f, c0, iterations, tolerance):
        x0 = c0
        self.table2 = []

        for i in range(iterations):
            d1f = derivative(f, x0, dx=1e-10, n=1)
            d2f = derivative(f, x0, dx=1e-10, n=2)
            x1 = x0 - ((d1f * f(x0)) / ((d1f) ** 2 - f(x0) * d2f))
            evaluated = f(x1)
            error = abs((x1 - x0) / x1) * 100
            self.table2.append([i + 1, x1, evaluated, error])

            if error <= tolerance:
                break

            x0 = x1

        table2 = np.array(self.table2)

        np.set_printoptions(precision=3)
        print("[i+1, x1, function evaluated, error]")
        print(table2)

        xi = table2[:, 1]
        yi = table2[:, 2]

        order = np.argsort(xi)
        xi = xi[order]
        yi = yi[order]

        plt.plot(xi, yi)
        plt.plot(xi, yi, "o")
        plt.axhline(0, color="black")

        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Newton-Raphson Multiple f(x)")
        plt.grid()
        plt.show()

    def false_position(self, f, lower, upper, iterations, tolerance):
        previous_iteration = 0
        self.table = []

        for i in range(iterations):
            if f(upper) - f(lower) == 0:
                print(
                    "Cannot divide by zero: f({})-f({})=0".format(
                        {f(upper)}, {f(lower)}
                    )
                )
                break

            current_iteration = upper + (
                f(upper) * (lower - upper) / (f(upper) - f(lower))
            )
            evaluated = f(current_iteration)
            error = (
                abs((current_iteration - previous_iteration) / current_iteration) * 100
            )
            self.table.append(
                [i + 1, current_iteration, evaluated, upper, lower, error]
            )

            if error <= tolerance:
                break

            if (f(lower) * f(current_iteration)) < 0:
                upper = current_iteration
            else:
                lower = current_iteration

            if (f(lower) * f(current_iteration)) == 0:
                print("Root found earlier than expected.")
                break

            previous_iteration = current_iteration

        table = np.array(self.table)
        np.set_printoptions(precision=3)
        print("[i+1, itr_act, f(c), lim_inf,  lim_sup,  error ]")
        print(table)

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
        plt.title("False Position f(c)")
        plt.grid()
        plt.show()

    def fixed_point(self, f, ci, iterations, tolerance):
        previous_iteration = ci
        self.table = []

        for i in range(iterations):
            current_iteration = f(previous_iteration)
            error = (
                abs((current_iteration - previous_iteration) / current_iteration) * 100
            )
            evaluated = f(current_iteration)
            self.table.append([i + 1, current_iteration, evaluated, error])

            if error <= tolerance:
                break

            previous_iteration = current_iteration

        table = np.array(self.table)
        np.set_printoptions(precision=3)
        print("[i+1, itr_act, f(c), lim_inf,  lim_sup,  error ]")
        print(table)

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
        plt.title("Iteration Fixed Point f(c)")
        plt.grid()
        plt.show()

    def secant(self, f, c0, c1, iterations, tolerance):
        x0 = c0
        x1 = c1
        self.table = []

        for i in range(iterations):
            x2 = x1 - ((f(x1) * (x0 - x1)) / (f(x0) - f(x1)))
            evaluated = f(x2)
            error = abs((x2 - x1) / x2) * 100
            self.table.append([i + 1, x2, evaluated, error])

            if error <= tolerance:
                break

            if evaluated == 0:
                print("Root found earlier than expected.")
                break

            x0 = x1
            x1 = x2

        table = np.array(self.table)
        np.set_printoptions(precision=3)
        print("[i, x2, function evaluated, error]")
        print(table)

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
        plt.title("Secant Method f(x)")
        plt.grid()
        plt.show()

    def standard_newton_raphson(self, f, ci, iterations, tolerance):
        previous_iteration = ci
        self.table = []

        for i in range(iterations):
            fx_evaluated = f(previous_iteration)
            fdx_evaluated = derivative(f, previous_iteration, dx=1e-10)

            if fdx_evaluated == 0:
                print("The derivative is zero.")
                break
            else:
                current_iteration = previous_iteration - (fx_evaluated / fdx_evaluated)

            function_evaluated = f(current_iteration)
            e = abs((current_iteration - previous_iteration) / current_iteration) * 100
            previous_iteration = current_iteration
            self.table.append(
                [i + 1, current_iteration, function_evaluated, previous_iteration, e]
            )

            if e <= tolerance:
                break

        table = np.array(self.table)
        np.set_printoptions(precision=3)
        print("[i+1, current_iteration, function_evaluated, previous_iteration, error]")
        print(table)

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
        plt.title("Standard Newton-Raphson f(x)")
        plt.grid()
        plt.show()


# Input
f = lambda x: np.cos(x)
function = Roots(f, 0.001)
function.standard_newton_raphson(f, 4, 7, 0)
