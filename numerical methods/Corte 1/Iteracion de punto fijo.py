# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 20:40:08 2022

@author: Cristian F. Zapata

"""
import numpy as np
import matplotlib.pyplot as plt


#Ieracion de punto fijo


f=lambda x: (3 +x -2*x**2)**(1/4)

def fijo(funcion,ci,ite, tolerancia):
  itr_ant=ci
  tabla=[]
  for i in range (ite):
    itr_act=f(itr_ant) #+itr_ant #si usted mismo despeja la x, comente la parte "+itr_ant"
    error=abs((itr_act-itr_ant)/itr_act)*100
    evalu=f(itr_act)
    tabla.append([i+1, itr_act, evalu, error])
    if error<=tolerancia:
        break
    itr_ant=itr_act
  return tabla

tabla=fijo(f, 1, 100 , 0.000001)
tabla = np.array(tabla)

#TABLA
np.set_printoptions(precision = 4) #AQUI PUEDE CAMBIAR UN NUMERO C.F, PERO LA
#TABLA SE HACE MUY GRANDE E INCOMODA DE VER.
print('[i, itr_act, evalu, error]')
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
plt.title('I. Punto fijo f(x)')
plt.grid()
plt.show()
