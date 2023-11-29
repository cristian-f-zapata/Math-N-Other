# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:44:26 2022

@author: Cristian F. Zapata
"""

#Aprendamos a graficar con Python
import numpy as np #Recordemos que Numpy me permite manipular matrices.
import matplotlib.pyplot as plt #Esta es la librería que me permite graficar.
#Para graficar funciones, pues hay que definir dichas funciones:
#Todas las funciones que serán graficadas deben ir en la parte superior, y para poder ser dibujadas en un mismo cuadro
#es decir, en el mismo intérvalo, pues todas ellas deben tener la misma variable, x.
funcion= lambda x: np.exp(x) -2
funcion2= lambda x:np.cos(np.exp(x)-2) #Recordar que se puede hacer uso de las funciones lambda, en cuyo caso seria: g=lamda x: np.cos(x)
  
#Entonces hago el intervalo para x, es importante definir eso porque de lo contrario esto se convertiria en un bucle infinito
#ya que no tendría una cota para suspender las ejecuciones.
x=np.linspace(0.1,1.5,100) #Donde el primero es donde empieza la gráfica, el segundo: donde termina. El tercero el número de puntos dentro del intérvalo.
#Una vez ya escrito los limites, debemos hacer nuestro espacio para que la gráfica se dibuje.
plt.plot(x,funcion(x),'purple',label='Funcion') #Solo basta con ejecutar para poder ver la función graficada. Se pone label, para darle como una etiqueta interna a la gráfica
#Para cambiar el color y la forma de la función, hacemos plt.plot(x,seno(x),'r#color#--#la forma#',label='Seno'), como se ve en la función de Coseno
#Y sirve para hacer legendas.
plt.plot(x,funcion2(x),'r--',label='funcion2')
#La gráfica hasta donde está, es inlegible, vamos a ponerle nombre a los ejes:
plt.xlabel('x')
plt.ylabel('Seno(x)')
#Título a la Gráfica
plt.title('Gráfica de Seno y Coseno en función de x')
#Si quiero que la gráfica tenga una cuadrícula, hacemos:
plt.grid()
#Podemos poner una legenda a la gráfica, siempre y cuando hayan más de una curvas en el espacio.
plt.legend()#Esto me sirve para poner leyendas a las gráficas. Poniendo plt.legend(loc=1,2,3 o 4), cambia la posición de la lengeda.
#Para poner texto dentro de la gráfica:
plt.text(0,0,'Hola')


