# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:40:32 2022

@author: gedes
"""

import numpy as np


# Integración: Regla de los trapecios



fx = lambda x: (np.exp(x)*np.sin(x))/(1+x**2)

list_romb=[]
list_romb2=[]

def trapecio(a,b,tramos): 
    h = (b-a)/tramos
    xi = a
    suma = fx(xi)
    for i in range(0,tramos-1,1):
        xi = xi + h
        suma = suma + 2*fx(xi)
    suma = suma + fx(b)
    area = h*(suma/2)
    
    return area
    

intervalos=[1,2,4,8]




def romberg(a,b,tramos):
    for i in range(s):
        if i < len(intervalos)-1:
            t1= trapecio(a,b,intervalos[i])
            t2= trapecio(a,b,intervalos[i+1])
            romb=(4/3)*t2-(1/3)*t1
            list_romb.append(romb)
    #parte 2
    for i in range(s):
        if i < len(list_romb)-1:
            t1= list_romb[i]
            t2= list_romb[i+1]
            romb=(4/3)*t2-(1/3)*t1
            list_romb2.append(romb)
    
    
    return list_romb2
    
romberg(a,b,tramos)

print(list_romb, list_romb2)   

    
    
    
    
    