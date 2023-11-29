# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:34:53 2022

@author: gedes
"""
import numpy as np
import matplotlib.pyplot as plt

f=lambda x: np.cos(2*x) + np.sin(3*x)
y=[]
x=[]
def euler(f,a,b,h,y0):
    i=int((b-a)/h)
    num=a
    for j in range(i):
        x.append(num)
        y.append(y0)
        yn=y0+f(num)*h
        y0=yn
        num=num+h
    return yn

print(euler(f,0,1,0.25,1))


xi = x
yi = y

# ordena los puntos para la grafica

plt.plot(xi,yi)
plt.plot(xi,yi,'o')
plt.axhline(0, color="black")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Método de Euler')
plt.grid()
plt.show()
print(x,y)