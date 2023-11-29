# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Metodo de Muller


from numpy import sign
from numpy.lib.scimath import sqrt
import matplotlib.pyplot as plt
import numpy as np

f=lambda x: np.exp(-x) - x**2 +np.sin(x)

def muller(f, x0, x1, x2, tol, it):
    i=1
    tabla=[]
    error = 1e3
    x3 = 0
    while error > tol:
        c = f(x2)
        b = ((x0 - x2)**2 * (f(x1) - f(x2)) - (x1 - x2)**2 *
             (f(x0) - f(x2))) / ((x0 - x2) * (x1 - x2) * (x0 - x1))
        a = ((x1 - x2) * (f(x0) - f(x2)) - (x0 - x2) *
             (f(x1) - f(x2))) / ((x0 - x2) * (x1 - x2) * (x0 - x1))
        x3 = x2 - (2 * c) / (b + sign(b) * sqrt(b**2 - 4 * a * c))
        error = abs(x3 - x2)
        tabla.append([i, x3, f(x3), error ])
        x0 = x1
        x1 = x2
        x2 = x3
        if it==i:
            break
        i=i+1
    return tabla


tabla=muller(f, 0, 0.5, 1, 10**(-1000),8)
tabla = np.array(tabla)

#TABLA
np.set_printoptions(precision = 3) #AQUI PUEDE CAMBIAR UN NUMERO C.F, PERO LA
#TABLA SE HACE MUY GRANDE E INCOMODA DE VER.
print('[i, x3, funcion evaluada, error ]')
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
plt.title('Metodo Muller f(x)')
plt.grid()
plt.show()



