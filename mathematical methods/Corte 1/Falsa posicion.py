# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 19:35:52 2022

@author: Cristian F. Zapata

"""
import numpy as np
import matplotlib.pyplot as plt 


#Falsa posicion


f=lambda x: x**2 -0.7

def regulafalsi (f,inf, sup,itr, tolerancia):
  itr_ant=0
  tabla=[]
  for i in range (itr):
    if f(sup)-f(inf)==0:
        print('No se puede dividir entre cero: f({})-f({})=0'.format({f(sup)},\
                                                                     {f(inf)}))
        break  
    itr_act=sup+(f(sup)*(inf-sup)/(f(sup)-f(inf)))
    evaluada=f(itr_act)
    error=abs((itr_act - itr_ant)/itr_act)*100
    tabla.append([i+1, itr_act,sup, inf, evaluada, error ])
    if error<=tolerancia:
        break
    if (f(inf)*f(itr_act))<0:
      sup=itr_act
    else:
      inf=itr_act
    if (f(inf)*f(itr_act))==0:
      print("Se ha encontrado la raiz antes de lo previsto.")
      break
    itr_ant=itr_act
  return tabla

tabla=regulafalsi(f,0.5,2,3,0.0000001)
tabla = np.array(tabla)

#TABLA
np.set_printoptions(precision = 3) #AQUI PUEDE CAMBIAR UN NUMERO C.F, PERO LA
#TABLA SE HACE MUY GRANDE E INCOMODA DE VER.
print('[i, itr_act,sup, inf, evaluada, error ]')
print(tabla)

xi = tabla[:,1]
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
plt.title('Falsa posicion f(x)')
plt.grid()
plt.show()