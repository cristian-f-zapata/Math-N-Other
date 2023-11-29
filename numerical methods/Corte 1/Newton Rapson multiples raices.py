# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:05:23 2022

@author: Cristian F. Zapata
"""

import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol 
from scipy.misc import derivative 

#N-R Para multiples raices 


f=lambda x: np.exp(-x) + x -2

def nrmultipe(f,c0,itr, tolerancia):
  x0=c0 
  tabla=[]
  for i in range (itr):
    d1f=derivative(f,x0,dx=1e-10,n=1)
    d2f=derivative(f,x0,dx=1e-10,n=2)
    x1=x0-((d1f*f(x0))/(((d1f)**2)-f(x0)*d2f))
    evalu=f(x1)
    error=abs((x1-x0)/x1)*100
    tabla.append([i+1, x1, evalu, error ]) 
    if error<=tolerancia:
        break
    x0=x1
  return tabla

tabla=nrmultipe(f, 1, 4, 0.0001)
tabla = np.array(tabla)

#TABLA
np.set_printoptions(precision = 3) #AQUI PUEDE CAMBIAR UN NUMERO C.F, PERO LA
#TABLA SE HACE MUY GRANDE E INCOMODA DE VER.
print('[i+1, x1, funcion evaluada, error ]')
print(tabla)

xi = tabla[:,1]
yi = tabla[:,2]

# ordena los puntos para la grafica
orden = np.argsort(xi)
xi = xi[orden]
yi = yi[orden]

plt.plot(xi,yi)
plt.plot(xi,yi,'o')
plt.axhline(0, color="black")

plt.xlabel('x')
plt.ylabel('y')
plt.title('N-R multiples f(x)')
plt.grid()
plt.show()
