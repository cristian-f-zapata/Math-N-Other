# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 21:41:47 2022

@author: Cristian F. Zapata

"""

import numpy as np
import matplotlib.pyplot as plt

v=500E3
n=1.81E-5
d=6E-3
p=874
g=9.81

def prom_vf(blata):
    tabla_tg_tef=blata
    tabla1=[]
    tabla=np.array(tabla_tg_tef)
    sin_cam=tabla[:, 0]
    con_cam=tabla[:, 1]
    prom_sin=sum(sin_cam)/3
    v_f=1/prom_sin
    return v_f
    
def prom_vr(blata):
    tabla_tg_ter=blata
    tabla1=[]
    tabla=np.array(tabla_tg_ter)
    sin_cam=tabla[:, 0]
    con_cam=tabla[:, 1]
    prom_con=sum(con_cam)/3
    v_r=1/prom_con
    return v_r
    

def q(blata):
    v_f=prom_vf(blata)
    v_r=prom_vr(blata)
    q=(v_f+v_r)*((v_f**(1/2))/(v))*(n**(3/2))*((18*np.pi*d)/((2*p*g)**(1/2)))
    return q


tabla_tg_te1=[[10.68, 4.96] , [11.28, 5.48], [11.72, 5.10]]
qgota1=q(tabla_tg_te1)
vf1=prom_vf(tabla_tg_te1)
vr1=prom_vr(tabla_tg_te1)

tabla_tg_te2=[[7.85, 4.67] , [6.68, 5.03], [6.31, 5.57]]
qgota2=q(tabla_tg_te2)
vf2=prom_vf(tabla_tg_te2)
vr2=prom_vr(tabla_tg_te2)

tabla_tg_te3=[[11.49, 2.26] , [10.97, 2.15], [11.86, 1.90]]
qgota3=q(tabla_tg_te3)
vf3=prom_vf(tabla_tg_te3)
vr3=prom_vr(tabla_tg_te3)


tabla_tg_te4=[[23.24, 2.53] , [20.49, 3.41], [22.20, 2.69]]
qgota4=q(tabla_tg_te4)
vf4=prom_vf(tabla_tg_te4)
vr4=prom_vr(tabla_tg_te4)


tabla_tg_te5=[[18.45, 2.90] , [18.38, 2.91], [18.42, 2.48]]
qgota5=q(tabla_tg_te5)
vf5=prom_vf(tabla_tg_te5)
vr5=prom_vr(tabla_tg_te5)


np.set_printoptions(precision = 4) 
print("Carga  V_f V_r ")
tablaf=[[qgota1, vf1, vr1], [qgota2, vf2, vr2], [qgota3, vf3, vr3], [qgota4, vf4, vr4], [qgota5, vf5, vr5]]
tabla=np.array(tablaf)
print(tabla)


# lista=[3.3463e-17, 3.3599e-17, 3.8698e-17, 5.1539e-17,  6.6404e-17]

# listaf=[1, 1.004064190299734, 1.1564414427875565, 1.5401787048381794, 1.98440068134955 ] 


