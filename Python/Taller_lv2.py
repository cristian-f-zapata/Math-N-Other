#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random as r
"""
Created on Thu Oct 28 18:30:31 2021

@author: Cristian F. Zapata
"""

#programa que calcula mediante aproximaciones las raices de un polinomio de grado n


A=[]
print("Para polinomios de la forma a+bx+cx**2+dx**3+...+(anx**n), (DEBE introducir\
los coeficientes en ese orden).")
n=eval(input("Ingrese grado del polinomio: "))+1
for i in range(n):
    print("Ingrese el coeficiente", i+1)
    valor=eval(input("."))
    A.append(valor) 
    
    #la lista vacia se llena con los n coeficientes introducidos por 
    #el usuario, si el grado del polinomio es n, el numero de coeficientes es 
    #n+1, debido al termino independiente 
B=[]
for i in range(len(A)):
    B.append(i*A[i]) 
    
    #la lista de los coeficintes de la funcion
# deribada es solo multiplicar los elementos de la lista A, por i, donde i va desde cero
#debido a que la derivada del termino constante es cero

x=eval(input("Ingrese valor inicial de x: ")) #este es el primer valor introducido por el usuario
x1=x #el primer valor que toma x1 es el introducido por el usuario
#posterior a ello, esta variable va a cambiar 
j=eval(input("¿Cuantas veces quiere repetir el procedimiento?: "))
for i in range(j):
    fx=[]
    for i in range(len(A)):
        fx.append((x1**(i))*(A[i])) #esta lista es equivalente a  la funcion
        #evaluada en x1, pero sin efectuar las sumas y restas
    dfx=[]
    for i in range(len(A)-1):
        dfx.append((B[i+1])*(x1**(i))) #esta lista es equivalente a la derivada 
        #de la funcion evaluada en x1
    sumaf=sum(fx)#valor de la funcion evaluada en x1
    sumadf=sum(dfx)#valor de la funcion derivada evaluada en x1
    Raiz=x1-(sumaf)/(sumadf) #con esta ecuacion se encuentran las aproximaciones
    x1=Raiz #el valor de x1 debe cambiar y repetise el procedimiento el numero de 
    #veces que uno quiera mejorar la aproximacion 
    if sumaf==0:
        break#la funcion evaluada en sus raices sera igual a caero, entonces
        #si ya se encontraron las raices, no es necesario continuar
print("Un numero raiz es: ",Raiz)  




#segundo punto

#programa que crea una lista de 1000 tuplas producidas de manera aleatoria
#el programa encuentra que tuplas estan encima, debajom y sobre la funcion


l=[]
for i in range(1000):
    l.append((r.randint(-10, 10), r.randint(0, 10)))
    #con esto se crea la lista con 1000 tuplas, con valores entre los valores 
    #que se plantea en el enunciado 
p_abajo=0
p_arriba=0
p_sobrefuncion=0 #estas banderas sirven para contar tuplas estan por encima o debajo 
for i in range(1000):
    if l[i][1]>(l[i][0])**2: #el valor x de la tupla, elevado al cuadrado 
    #es un valor utilizado como referencia, si el valor y de la tupla es mayor 
    #a el valor de x al cuadrado, entonces esta tupla esta por encima de la funcion
        p_arriba=p_arriba+1 #cada vez que se cumpla, se suma 1 a la bandera 
    elif l[i][1]<(l[i][0])**2: #si el valor de x al cuadrado es mayor al valor de y 
    #de la tupla, esta tula esta por debajo de la funcion
        p_abajo=p_abajo+1#cada vez que se cumpla, se suma 1 a la bandera
    elif l[i][1]==(l[i][0])**2:#si el valor de x al cuadrado es el mismo que el valor de 
    #y de la tupla, entonces esta tupla esta sobre la funcion
        p_sobrefuncion=p_sobrefuncion+1#cada vez que se cumpla, se suma 1 a la bandera
print("Hay ",p_abajo, " puntos abajo de la función,", "hay " , p_arriba," puntos\
 arriba de la funcion, " ,"y hay " , p_sobrefuncion, " puntos sobre la funcion.")











