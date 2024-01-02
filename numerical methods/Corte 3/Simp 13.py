"""
Created on Sun Jan 29 12:25:02 2023

@author: cristian
"""
# Integration: Simpson's 1/3 Rule
# Ensure the number of intervals is even
import numpy as np
import matplotlib.pyplot as plt

# INPUT
fx = lambda x: np.sqrt(x) * np.sin(x)

# integration interval
a = 1
b = 3
intervals = 8

# Ensure the number of intervals is even
is_odd = intervals % 2
while is_odd == 1:
    intervals = int(input("Intervals should be even: "))
    is_odd = intervals % 2

# PROCEDURE
# Simpson's 1/3 Rule, multiple intervals
h = (b - a) / intervals
xi = a
# iterate over every two intervals
sum_result = fx(xi)
for i in range(0, intervals - 2, 2):
    xi = xi + h
    sum_result = sum_result + 4 * fx(xi)
    xi = xi + h
    sum_result = sum_result + 2 * fx(xi)
# last interval
xi = xi + h
sum_result = sum_result + 4 * fx(xi)
sum_result = sum_result + fx(b)
area = (h / 3) * sum_result

# OUTPUT
print("Intervals: ", intervals)
print("Integral: ", area)
