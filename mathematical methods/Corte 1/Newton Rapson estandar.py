# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 17:47:01 2022

@author: Cristian F. Zapata

"""
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from scipy.misc import derivative



#N-R Estandar


x=sp.Symbol("x")
f_=lambda x: np.exp(-x)+ x -2

def nr_estandar(f, ci, itr, tolerancia):
  itr_ant=ci
  tabla=[]
  for i in range (itr):
    fx_evaluado=f(itr_ant)
    fdx_evaluado=derivative(f, itr_ant, dx=1e-10)              
    if fdx_evaluado==0:
        print("La derivada es cero.")
        break
    else:
        itr_act=itr_ant-(fx_evaluado/fdx_evaluado)
    funcion_evalu=f(itr_act)
    e=abs((itr_act - itr_ant)/itr_act)*100
    itr_ant=itr_act
    tabla.append([i+1,itr_act,itr_ant, funcion_evalu, e])
    if e<=tolerancia:
        break
  return tabla

tabla=nr_estandar(f_, 1, 4,0.000001)
tabla = np.array(tabla)

#TABLA
np.set_printoptions(precision = 3) #AQUI PUEDE CAMBIAR UN NUMERO C.F, PERO LA
#TABLA SE HACE MUY GRANDE E INCOMODA DE VER.
print('[i+1,itr_act,itr_ant, funcion_evalu, error]')
print(tabla)

xi = tabla[:,1]
yi = tabla[:,3]

# ordena los puntos para la grafica
orden = np.argsort(xi)
xi = xi[orden]
yi = yi[orden]

plt.plot(xi,yi)
plt.plot(xi,yi,'o')
plt.axhline(0, color="black")

plt.xlabel('x')
plt.ylabel('y')
plt.title('N-R estandar f(x)')
plt.grid()
plt.show()