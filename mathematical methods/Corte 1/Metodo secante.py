# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 19:06:02 2022

@author: Cristian F. Zapata

"""
from logging import error
import matplotlib.pyplot as plt
import numpy as np


#Metodo secante


f=lambda x: np.exp(-x)+x-2

def secante(f,c0,c1,itr, tolerancia):
  x0=c0
  x1=c1
  tabla=[]
  for i in range (itr):
    x2=x1-((f(x1)*(x0-x1))/(f(x0)-f(x1)))
    evaluado=f(x2)
    error=abs((x2-x1)/x2)*100
    tabla.append([i+1,x2, evaluado, error ])
    if error<=tolerancia:
        break
    if evaluado==0:
        print("Se ha encontrado la raiz antes de lo esperado")
        break
    x0=x1
    x1=x2
  return tabla

tabla=secante(f,1,2,4, 0.00000001)
tabla = np.array(tabla)

#TABLA
np.set_printoptions(precision = 3) #AQUI PUEDE CAMBIAR UN NUMERO C.F, PERO LA
#TABLA SE HACE MUY GRANDE E INCOMODA DE VER.
print('[i, x2, funcion evaluada, error]')
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
plt.title('Metodo secante f(x)')
plt.grid()
plt.show()