# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:40:32 2022

@author: cristian F. Zapata
"""
import numpy as np

fx = lambda x: (np.exp(x) * np.sin(x)) / (1 + x**2)

list_romb = []
list_romb2 = []


def trapecio(a, b, tramos):
    h = (b - a) / tramos
    xi = a
    suma = fx(xi)
    for i in range(0, tramos - 1, 1):
        xi = xi + h
        suma = suma + 2 * fx(xi)
    suma = suma + fx(b)
    area = h * (suma / 2)

    return area


a = 0
b = 1
tramos = [1, 2, 4, 8]


def romberg(a, b, tramos):
    for i in range(len(tramos) - 1):
        t1 = trapecio(a, b, tramos[i])
        t2 = trapecio(a, b, tramos[i + 1])
        romb = (4 / 3) * t2 - (1 / 3) * t1
        list_romb.append(romb)

    for i in range(len(list_romb) - 1):
        t1 = list_romb[i]
        t2 = list_romb[i + 1]
        romb = (4 / 3) * t2 - (1 / 3) * t1
        list_romb2.append(romb)

    return list_romb2


result = romberg(a, b, tramos)
print(result)
