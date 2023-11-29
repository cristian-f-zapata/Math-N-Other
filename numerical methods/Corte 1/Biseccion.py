# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 20:58:02 2022

@author: Cristian F. Zapata


"""
import matplotlib.pyplot as plt
import numpy as np


#biseccion


function=lambda x: np.exp(-x)+np.cos(x)-np.log(x)

def biseccion(function, lim_inf, lim_sup, itr, tolerancia):
  itr_ant=0
  tabla=[]
  for i in range(itr):
    itr_act=(lim_inf + lim_sup)/2
    funcion_evalu=function(itr_act)
    e=abs((itr_act - itr_ant)/itr_act)*100
    tabla.append([i+1,lim_inf,itr_act,lim_sup, funcion_evalu, e])
    if e<=tolerancia:
        break
    if (function(lim_inf)*function(itr_act))<0:
      lim_sup=itr_act
    else:
      lim_inf=itr_act
    itr_ant=itr_act
  return tabla

tabla=biseccion(function, 0.5, 1.5, 5, 0.001)
tabla = np.array(tabla)

#TABLA
np.set_printoptions(precision = 3) #AQUI PUEDE CAMBIAR UN NUMERO C.F, PERO LA
#TABLA SE HACE MUY GRANDE E INCOMODA DE VER.
print('[i+1, lim_inf, itr_act, lim_sup, f(c), error ]')
print(tabla)

xi = tabla[:,2]
yi = tabla[:,4]

# ordena los puntos para la grafica
orden = np.argsort(xi)
xi = xi[orden]
yi = yi[orden]

plt.plot(xi,yi)
plt.plot(xi,yi,'o')
plt.axhline(0, color="black")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Bisección en f(x)')
plt.grid()
plt.show()