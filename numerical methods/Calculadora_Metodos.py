#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 12:25:02 2023

@author: cristian
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative 


class Metodos_Numericos:
    pass
    def __init__(self,f, tolerancia):
        self.f=f
        self.tolerancia=tolerancia
 
class raices(Metodos_Numericos):

    def biseccion(self,f, lim_inf, lim_sup, itr, tolerancia):
        itr_ant=0
        self.tabla=[]
        for i in range(itr):
          itr_act=(lim_inf + lim_sup)/2
          funcion_evalu=f(itr_act)
          e=abs((itr_act - itr_ant)/itr_act)*100
          self.tabla.append([i+1,  itr_act, funcion_evalu, lim_inf,lim_sup,  e])
          if e<=tolerancia:
              break
          if (f(lim_inf)*f(itr_act))<0:
            lim_sup=itr_act
          else:
            lim_inf=itr_act
          itr_ant=itr_act
        
        tabla = np.array(self.tabla)
        
        np.set_printoptions(precision = 3) #AQUI PUEDE CAMBIAR UN NUMERO C.F, PERO LA
                #TABLA SE HACE MUY GRANDE E INCOMODA DE VER.
        print('[i+1, itr_act, f(c), lim_inf,  lim_sup,  error ]')
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
        plt.title('biseccion f(c)')
        plt.grid()
        plt.show()

    def NR_Muliple(self,f,c0,itr, tolerancia):
        x0=c0 
        self.tabla2=[]
        for i in range (itr):
            d1f=derivative(f,x0,dx=1e-10,n=1)
            d2f=derivative(f,x0,dx=1e-10,n=2)
            x1=x0-((d1f*f(x0))/(((d1f)**2)-f(x0)*d2f))
            evalu=f(x1)
            error=abs((x1-x0)/x1)*100
            self.tabla2.append([i+1, x1, evalu, error ]) 
            if error<=tolerancia:
                break
            x0=x1
        tabla2 = np.array(self.tabla2)

        np.set_printoptions(precision = 3) 
        print('[i+1, x1, funcion evaluada, error ]')
        print(tabla2)
    
        xi = tabla2[:,1]
        yi = tabla2[:,2]
    
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
        

    def regulafalsi (self,f, inf, sup,itr, tolerancia):
      itr_ant=0
      self.tabla=[]
      for i in range (itr):
        if f(sup)-f(inf)==0:
            print('No se puede dividir entre cero: f({})-f({})=0'.format({f(sup)},\
                                                                         {f(inf)}))
            break  
        itr_act=sup+(f(sup)*(inf-sup)/(f(sup)-f(inf)))
        evaluada=f(itr_act)
        error=abs((itr_act - itr_ant)/itr_act)*100
        self.tabla.append([i+1, itr_act,evaluada,  sup, inf, error ])
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
      tabla = np.array(self.tabla)
      np.set_printoptions(precision = 3) 
      print('[i+1, itr_act, f(c), lim_inf,  lim_sup,  error ]')
      print(tabla)
              
      xi = tabla[:,1]
      yi = tabla[:,2]
              
      orden = np.argsort(xi)
      xi = xi[orden]
      yi = yi[orden]
              
      plt.plot(xi,yi)
      plt.plot(xi,yi,'o')
      plt.axhline(0, color="black")
              
      plt.xlabel('x')
      plt.ylabel('y')
      plt.title('regula falsi f(c)')
      plt.grid()
      plt.show()
    
    
    def fijo(self, f ,ci,ite, tolerancia):
        itr_ant=ci
        self.tabla=[]
        for i in range (ite):
            itr_act=f(itr_ant) #+itr_ant #si usted mismo despeja la x, comente la parte "+itr_ant"
            error=abs((itr_act-itr_ant)/itr_act)*100
            evalu=f(itr_act)
            self.tabla.append([i+1, itr_act, evalu, error])
            if error<=tolerancia:
                break
            itr_ant=itr_act
        tabla = np.array(self.tabla)
        np.set_printoptions(precision = 3) 
        print('[i+1, itr_act, f(c), lim_inf,  lim_sup,  error ]')
        print(tabla)
                
        xi = tabla[:,1]
        yi = tabla[:,2]
                
        orden = np.argsort(xi)
        xi = xi[orden]
        yi = yi[orden]
                
        plt.plot(xi,yi)
        plt.plot(xi,yi,'o')
        plt.axhline(0, color="black")
                
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Iteracion punto fijo f(c)')
        plt.grid()
        plt.show()

    
    def secante(self, f,c0,c1,itr, tolerancia):
        
        x0=c0
        x1=c1
        self.tabla=[]
        for i in range (itr):
          x2=x1-((f(x1)*(x0-x1))/(f(x0)-f(x1)))
          evaluado=f(x2)
          error=abs((x2-x1)/x2)*100
          self.tabla.append([i+1,x2, evaluado, error ])
          if error<=tolerancia:
              break
          if evaluado==0:
              print("Se ha encontrado la raiz antes de lo esperado")
              break
          x0=x1
          x1=x2
        tabla = np.array(self.tabla)

        np.set_printoptions(precision = 3) 
        print('[i, x2, funcion evaluada, error]')
        print(tabla)

        xi = tabla[:,1]
        yi = tabla[:,2]

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
        

    def NR_estandar(self, f, ci, itr, tolerancia):
      itr_ant=ci
      self.tabla=[]
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
        self.tabla.append([i+1,itr_act, funcion_evalu, itr_ant,  e])
        if e<=tolerancia:
            break
        
      tabla = np.array(self.tabla)
      np.set_printoptions(precision = 3) 
      print('[i+1,itr_act, funcion_evalu, itr_ant, error]')
      print(tabla)

      xi = tabla[:,1]
      yi = tabla[:,2]

      orden = np.argsort(xi)
      xi = xi[orden]
      yi = yi[orden]
      
      plt.plot(xi,yi)
      plt.plot(xi,yi,'o')
      plt.axhline(0, color="black")

      plt.xlabel('x')
      plt.ylabel('y')
      plt.title('NR_estandar f(x)')
      plt.grid()
      plt.show()
    
        
#Input        
        
f=lambda x: np.cos(x)
funcion=raices(f,0.001)
funcion.NR_estandar(f, 4, 7, 0)
