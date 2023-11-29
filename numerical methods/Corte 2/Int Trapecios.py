#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 22:48:24 2022

@author: cristian
"""

import numpy as np
import matplotlib.pyplot as plt



# Integración: Regla de los trapecios



fx = lambda x: np.sin(x**2)

a = 0
b = np.pi/2
tramos = 6


h = (b-a)/tramos
xi = a
suma = fx(xi)
for i in range(0,tramos-1,1):
    xi = xi + h
    suma = suma + 2*fx(xi)
suma = suma + fx(b)
area = h*(suma/2)

print('tramos: ', tramos)
print('Integral: ', area)


muestras = tramos + 1
xi = np.linspace(a,b,muestras)
fi = fx(xi)
# Linea suave
muestraslinea = tramos*10 + 1
xk = np.linspace(a,b,muestraslinea)
fk = fx(xk)


plt.plot(xk,fk, label ='f(x)')
plt.plot(xi,fi, marker='o',
         color='orange', label ='muestras')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Integral: Regla de Trapecios')
plt.legend()

# Trapecios
plt.fill_between(xi,0,fi, color='r')
for i in range(1,muestras,1):   #o0
    plt.axvline(xi[i], color='w')

plt.show()