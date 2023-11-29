#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 16:41:58 2022

@author: cristian
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


# Interpolacion de Lagrange



xi = [2, 2.75, 4]
fi = []

for i in range(len(xi)):
    feval=lambda x: 1/x       #Aqui pone la funcion por si no te dan valores de f(x)
    feval=feval(xi[i])
    fi.append(feval)

xi = np.array(xi)
fi = np.array(fi)


n = len(xi)
x = sym.Symbol('x')
polinomio = 0
divisorL = np.zeros(n, dtype = float)

for i in range(0,n,1):
    numerador = 1
    denominador = 1
    for j  in range(0,n,1):
        if (j!=i):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i]-xi[j])
    terminoLi = numerador/denominador

    polinomio = polinomio + terminoLi*fi[i]
    divisorL[i] = denominador

polisimple = polinomio.expand()

px = sym.lambdify(x,polisimple)

muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a,b,muestras)
pfi = px(pxi)

print("****************************************************************************")
print('    valores de fi: ',fi)
print('divisores en L(i): ',divisorL)
print("****************************************************************************")
print('Polinomio de Lagrange, completo')
print(polinomio)
print("****************************************************************************")
print('Polinomio de Lagrange: ')
print(polisimple)
print("****************************************************************************")

plt.plot(xi,fi,'o', label = 'Puntos')
plt.plot(pxi,pfi, label = 'Polinomio')
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Interpolación Lagrange f(x)')
plt.show()