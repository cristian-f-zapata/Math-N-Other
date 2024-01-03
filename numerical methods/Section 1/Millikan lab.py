# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 21:41:47 2022

@author: Cristian F. Zapata

"""

import numpy as np


def calculate_quantities(table):
    sin_cam = table[:, 0]
    con_cam = table[:, 1]

    prom_sin = sum(sin_cam) / 3
    prom_con = sum(con_cam) / 3

    v_f = 1 / prom_sin
    v_r = 1 / prom_con

    q = (
        (v_f + v_r)
        * ((v_f ** (1 / 2)) / v)
        * (n ** (3 / 2))
        * ((18 * np.pi * d) / ((2 * p * g) ** (1 / 2)))
    )

    return q, v_f, v_r


def print_table(table):
    np.set_printoptions(precision=4)
    print("Carga  V_f  V_r")
    print(table)


# Experiment Data
table_data = [
    [[10.68, 4.96], [11.28, 5.48], [11.72, 5.10]],
    [[7.85, 4.67], [6.68, 5.03], [6.31, 5.57]],
    [[11.49, 2.26], [10.97, 2.15], [11.86, 1.90]],
    [[23.24, 2.53], [20.49, 3.41], [22.20, 2.69]],
    [[18.45, 2.90], [18.38, 2.91], [18.42, 2.48]],
]

# Constants
v = 500e3
n = 1.81e-5
d = 6e-3
p = 874
g = 9.81

# Calculate Quantities for Each Experiment
results_table = []
for i, experiment_data in enumerate(table_data, start=1):
    qgota, vf, vr = calculate_quantities(np.array(experiment_data))
    results_table.append([f"Experiment {i}", qgota, vf, vr])

# Display Results
print_table(np.array(results_table))
