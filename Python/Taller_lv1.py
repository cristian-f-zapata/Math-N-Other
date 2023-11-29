# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 10:53:44 2021

@author: cfzap
"""
import numpy as np
from scipy import linalg as LA
import random as r
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

#Funciones:
    
def mcd(a,b):
 while a % b != 0:
     a, b = b, a % b
 return b

def grados(g):
    return m.sin(m.radians(g))

def cadena(a,b,c):
    print("{0} quiere a {1}, pero no a {2}, y {1} quiere a {2}, pero no a {0}".format(a,b,c))


def crea_matriz(fil,col):
    print("")
    f=-1;c=-1
    e_fil=[]
    for f in range(fil):
        e_col=[]
        f+=1
        for c in range(col):
            c+=1
            valor=input('Introduzca el componente (%d,%d): '%(f,c))
            e_col.append(valor)
        e_fil.append(e_col)
        matri=np.array(e_fil,float)
    return matri
if __name__=="__main__":
    
    "1"
    # Realizar un programa que calcule el MCD, para ello use elalgoritmo de Euclides
    # •Primero calcule el residuo de dividir el número más grande por elnúmero más pequeño
    # •Luego, reemplace el número más grande con el número máspequeño y el número más pequeño
    # con el residuo.•Repita este proceso hasta que el número menor sea 0. 
    # El MCD esel último residuo diferente de
        
    print(mcd(8,3))
    print("***********************************")
    
    
    "2"      
    # Escribir un programa que solicite el nombre de tres productos y
    # el rango de precios de cada uno e imprima en una cadena conformato 
    # un texto donde se describa detalladamente losproductos, con sus precios
    # y los rangos ingresados. Debe usarseuna cadena con formato, generarsen 
    # los precios de formaaleatoria y usarlos en el texto más de una vez.
    
    pro1=input("ingrese nombre de producto uno: ")
    a1=eval(input("ingrese rango inferior: "))
    a2=eval(input("ingrese rango superior:  "))
    pre1=r.randint(a1, a2)
    pro2=input("ingrese nombre de producto dos: ")
    b1=eval(input("ingrese rango inferior: "))
    b2=eval(input("ingrese rango superior:  "))
    pre2=r.randint(b1, b2)
    pro3=input("ingrese nombre de producto tres: ")
    c1=eval(input("ingrese rango inferior: "))
    c2=eval(input("ingrese rango superior:  "))
    pre3=r.randint(c1, c2)
    print("El precio de {0} es {1} pesos, el precio de {2} es {3} pesos, y \
    finalmente, {4} cuesta {5}" .format(pro1, pre1, pro2, pre2, pro3, pre3))
    print("***********************************")
    
    
    "3"
    # Escribir un programa que calcule elsinnθpara un ánguloingresado por el 
    # usuario y unnaleatorio entero e imprima larespuesta con diferentes opciones 
    # de formato
    
    n=r.randint(0,1000)
    angulo=eval(input("ingrese argumento de la funcion seno: "))
    operacion=(m.sin(angulo))**n
    print("para el angulo {0} y el exponente {1}, la funcion seno tiene el valor \
    de {2}" .format(angulo, n, operacion)) 
    print("***********************************")
    
    
    "4"
    # Escriba un programa en que el usuario ingrese dos caracteres (opalabras) y
    # sean usados como separadores y como final de líneaen comandos print
    
    separador=input("ingrese separador: ")
    print("Este", "es", "texto", "prueva", sep=separador, end=separador)
    print("***********************************")
    
    "5"
    # Pregunte al usuario el precio de la comida y el porcentaje depropina que 
    # quiere dejar. Luego imprima tanto el monto de lapropina como el total de la 
    # factura con la propina incluida.
    
    comida=eval(input("ingrese precio de la comida: "))
    porcentaje=eval(input("¿cual es el porcentaje de propina?: "))
    propina=(comida/100)*porcentaje
    total=comida+propina
    print("el precio de la comida es {0}, el de la propina es {1}, entonces el\
    precio total a pagar es {2}".format(comida, propina, total))
    print("***********************************")
    
    
    "6"
    # Escriba un programa que calcule512−28248∗48+5πcon el número decifras 
    # decimales que el usuario desee
    
    cifras=eval(input("ingrese numero de cifras"))
    n=(521-528)/(48*48+5*(m.pi))
    print("con {0} cifras decimales, el valor para la operacion es {1:.{0}f}"\
    .format(cifras, n))
    print("***********************************") 
        
    "7"    
    # Escriba un programa que pase de grados farenheit a centigrados
    
    f=eval(input("ingrese temperatura el F°: "))
    ope=(f-32)*(5/9)
    print("{0} F°  equivale a {1} C°" .format(f, ope)) 
    print("***********************************")
    
    
    "8"
    # Pidale al usuario un númeroxe imprima (usando el argumentosep)x−−−2x−−−30−−−4x−−−5x
   
    x=eval(input("ingrese numero: "))
    print(x,2*x,3*x,4*x,5*x, sep="---")
    print("***********************************")
    
    
    "9"
    # Escriba un programa que le pida al usuario que ingrese tresnúmeros. 
    # Cree variables llamadas total y promedio quecontengan la suma y el promedio 
    # de los tres números e imprimalos valores de total y promedio.
    
    num1=eval(input("ingrese numero uno: "))
    num2=eval(input("ingrese numero dos: "))
    num3=eval(input("ingrese numero tres: "))
    total=num1+num2+num3
    promedio=total/3
    print("la suma de los numeros es {0} y su promedio es {1}".format(total, promedio))
    print("***********************************")
    
    
    "10"
    # funcion que funcione con grados
    
    print(grados(25))
    print("***********************************")
    
    
    "11"
    # funcion que imprima cadena con formato con cierta informacion 
    
    cadena("perro", "gato", "mico")
    print("***********************************")
    
    
    "12"
    # Escribir un programa que solicite el nivel de Ph y si está entre0−4decir 
    # que es un ácido fuerte,5−6ácido debil,7neutral,8−9base debil y10−14base fuerte
    
    ph=eval(input("Ingrese valor de ph: "))
    if 0<=ph<=4:
        print("Es un acido fuerte")
    elif 5<=ph<=6:
        print("Es un acido debil")
    elif ph==7:
        print("Es una sustancia neutra")
    elif 8<=ph<=9:
        print("Es una base debil")
    elif 10<=ph<=14:
        print("Es una base fuerte ")
    else:
        print("el ph esta fuera del rango permitido")
    print("***********************************")
    
    
    "13"
    # Escribe un programa de juegos de multiplicación para niños. Elprograma 
    # debe dar al jugador diez preguntas de multiplicacióngeneradas al azar. 
    # Después de cada uno, el programa debedecirles si lo hicieron bien o mal y 
    # cuál es la respuesta correcta.
   
    b=0
    for i in range(5):
        n1=r.randint(-10,10)
        n2=r.randint(-10,10)
        mul=n1*n2
        pre=eval(input("¿cuanto es la multiplicacion de {0} por {1}".format(n1,n2)))
        if pre==mul:
            b=b+1
            print("Muy bien, llevas {0} resuestas correctas de {1}".format(b, i+1))
        else:
            print("Lo siento :c, no es correcto. La respuesta correcta es {0}. \
            llevas {1} correctas de {2}" .format(mul, b, i+1 ))
    if b==5:
        print("Wow, eres muuuy bueno :0")
    print("***********************************")
    
        
    "14"   
    # Escriba un juego que le permita al usuario jugar piedra papel otijera cierto 
    # numero de rondas y al final diga el marcador.
   
    print("Piedra: 0, papel: 1 o tijera: 2")
    n=0
    e=0
    d=0
    for i in range(5):
        jugador=eval(input("¿piedra,papel o tijera?: "))
        maquina=r.randint(0,2)
        piedra=0
        papel=1
        tijera=2
        if maquina==jugador:
            print("Empate 0.o")
            e=e+1
        elif jugador==0 and maquina==2:
            print("Ganaste")
            n=n+1
        elif jugador==0 and maquina==1:
            print("pierdes")
            d=d+1
        elif jugador==1 and maquina==0:
            print("Ganaste")
            n=n+1
        elif jugador==1 and maquina==2:
            print("pierdes")
            d=d+1
        elif jugador==2 and maquina==1:
            print("Ganaste")
            n=n+1
        elif jugador==2 and maquina==0:
            print("pierdes")
            d=d+1
    print("Final de juego, hubieron {0} veces que ganas, {2} que pierdes y \
        {1} empates".format(n, e, d))
    print("***********************************")
    
    
    "15"
    # Escriba un programa que le pida al usuario que ingrese un número e imprima 
    # todos los divisores de ese número
    
    print("te digo cuales son los divisores de un numero desde uno hasta el\
    numero que introduscas")    
    n=eval(input("Introduce el numero: "))
    for i in range(n):
        operacion=n%(i+1)
        if operacion==0:
            print("{0} es un divisor de {1}". format(i+1, n))
        else:
            print("{0} no es un divisor de {1}". format(i+1, n))
    print("***********************************")

      
    "16"        
    # Escriba un programa que le permita al usuario pasar unatemperatura de 
    # grados centígrados, farenheit o Kelvin a laescala térmica que el desee.    
    
    print("convierto de grados centigrados a farenheit o kelvin")
    decision=input("¿Convertir a farenheit o a kelvin?: ")
    if decision=="farenheit":
        c=eval(input("introdusca temperatura: "))
        ope1=(c)*(9/5)+32
        print("El resrltado es: ", ope1,"F°")
    elif decision=="kelvin":
        c2=eval(input("introdusca temperatura: "))
        ope2=(c2)+273.15
        print("El resrltado es: ", ope2, "K°")
    else:
        print("no ha  elegido uno de los  parametros adecuados")
    print("***********************************")
    
    
    "17"   
    # Realice un juego en el que el usuario deba adivinar un númerosecreto 
    # (generado por el programa) el cual
    # 1.Dure5turnos
    # 2.Le diga si el número a adivinar es mayor o menor que el que dijo
    # 3.Le informe al usuario cuando gane 
    # o pierda (Inmediatamente)Realice el algoritmo con for y con while.Ayuda:En 
    # uno de los casosno es necesario usar el comando break
    
    n=r.randint(0,5)
    n=0
    for i in range(5):
        intento=eval(input("introdusca un numero: "))
        if intento==n:
            print("ganaste")
            n=n+1
            break
        else:
            print("fallaste")
    if n==0:
        print("maximo de intentos alcanzado")
    else:
        print("fin de juego")
    print("***********************************")
    
    
    "18"
    # Realice un programa que diga si un número ingresado es o no primo.Use el break
    
    numero=eval(input("introdusca numero: "))
    n=0
    for i in range(numero):
       div=numero%(i+1)
       if div==0:
           n=n+1
       elif n==3:
           break
    if n==2:
        print("el numero es primo")
    else:
        print("el numero no es primo")
    print("***********************************")
    
    
    "19"    
    # Hay un antiguo método para calcular (aproximar) la raizcuadrada de un número dadox.
    # Se parte de una conjeturaay secalculaa+xa2. Este resultado es la primera aproximación,
    # pero elresultado se puede refinar aún más tomando como ansatz esteresultado y repitiendo
    # el procedimiento las veces que sea.Realice un programa que calcule la raíz cuadrada de 
    # un númerodado y lo haga con la precisión que desee el usuario.No puedehacer uso de la 
    # librería math. 
    
    numero=eval(input("ingrese numero"))
    n=eval(input("ingrese presicion"))
    if numero>=0:
        p=numero
        i=0
        while i<=n and i!=p:
            i=p
            p=(numero/p+p)/2
        print("El resultado es:", p)
    print("***********************************")
    
    
    "20"
    # escriba un  programa que le pida al usuario diez numeros y digale cual es el mayor y menor
    
    a=[]
    for i in range(10):
        n=eval(input("Ingresa un numero: "))
        a.append(n)
    print(a)
    m=min(a)
    M=max(a)
    print("el valor minimo de la lista es {0}, y el valor maximo es {1}".format(m, M))
    print("***********************************")
    
    
    
    "21"
    # convierta de kilogramos a libras, asegurese que el dato sea correcto
    
    valor=eval(input("ingrese valor en kilogramos: "))
    if valor<0:
        print("El valor no tiene sentido fisico")
    else:
        n=valor/2
        print("{0} kilogramos equivale a {1} libras".format(valor, n))
    print("***********************************")
    
    
    "22"
    # estudiante puede ingresa la cantidad que quiera de notas, terminando con un
    # negativo, el programa indica nota mas baja, alta y promedio.
    
    notas=[]
    
    for i in range(999):
        nota=eval(input("ingrese nota: "))
        if nota<0:
            print("la nota mas alta es {0}, la mas baja es {1}, y el promedio\
            de las notas es {2}".format(M, m, promedio))
            break
        elif 0<nota<=5:
            notas.append(nota)
            m=min(notas)
            M=max(notas)
            s=sum(notas)
            promedio=s/(i+1) 
    print("***********************************")
    
    
    "23"
    # ingresa lista de numeros enteros y, imprima numero total de elementos, 
    # imprima el ultimo elemento de la lista, impima la lista en orden inverso, 
    # imprima si la lista contiene un numero 5, imprima el numero 5 de la lista, 
    # elimine el primer y ultimo elemento de la lista y ordene los elementos 
    # restantes e imprima el resultado 
    
    lista=[]
    
    for i in range(999):
        try:
            dato=int(input("ingrese dato: "))
            lista.append(dato)
            pregunta=input("¿desea continuar?: ")
            if pregunta=="si":
                2
            elif pregunta=="no":
                break
        except:
            print("el valor no es un entero")
    for i in range(len(lista)):
        if lista[i]==5:
            print("la lista tiene al menos un numero 5")
    if len(lista)>=5:
        cinco=lista[5]
        tamaño=len(lista)
        ultimo=lista[-1]
        inversa=reversed(lista)
        print(lista, ultimo, tamaño, cinco)
        del list[0]
        del list[-1]
        print(lista)
    print("***********************************")
    
    
    
    "24"
    # Escriba un programa que le pida al usuario una hora entre la 1 ylas 12,
    # le pida que ingrese am o pm y le pregunte cuántas horasen el futuro quiere 
    # ir. Imprima cuál será la hora dentro de tantashoras en el futuro, imprimiendo
    # am o pm según corresponda. Acontinuación se muestra un ejemplo. (Se pueden 
    # ingresarnúmero mucho mayores a 24)
    
    hora_actual=eval(input("ingrese hora actual: "))
    minutos=eval(input("ingrese minutos: "))
    zona=input("¿am o pm?")
    tiempo=eval(input("¿cuantas horas quiere adelantar?: "))
    minutos_adelanto=eval(input("ingrese minutos: "))
    
    minutos_totales=minutos+minutos_adelanto
    zonat=0
    if zona=="am":
        zonat=1
    elif zona=="pm":
        zonat=2
    hora_total=hora_actual+tiempo
    n=1
    for i in range(hora_total):
        n=n+1
        if n>=12:
            zonat=zonat+1
            n=1
    am_pm=" "
    if zonat%2==0:
        am_pm="pm"
    else:
        am_pm="am"
        
    hora=0
    for i in range(hora_total):
        hora=hora+1
        if hora>12:
            hora=1
    minutos_resultado=0
    if minutos_totales>=60:
        minutos_resultado=minutos_totales-60
        hora=hora+1
    elif minutos_totales<60:
        minutos_resultado=minutos_totales
    print("la hora es {0}:{2} {1}".format(hora,am_pm, minutos_resultado))
    print("***********************************")
    
    
    
    "25"
    # La lista [’a’, ’bb’, ’ccc’, ’dddd’,. . . ] que termina con 26 copias de laletra z.
    
    a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p",\
        "q","r","s","t","v","w","x","y","z"]
    for i in range(len(a)):
        a.append(i*a[i])
    print(a)
    print("***********************************")
    
    
    
    "26"
    # Escriba un programa que tome dos listas L y M del mismotamaño y sume sus
    # elementos para formar una nueva lista Ncuyos elementos sean sumas de los 
    # elementoscorrespondientes en L y M. Por ejemplo, si L = [3,1, 4] y M = [1,5,9],
    # entonces N debería ser igual a [4,6,13].
    
    a=[]
    b=[]
    for i in range(10):
        a.append(r.randint(0,100))
        b.append(r.randint(0,100))
    print(a, b)
    c=[]
    for i in range(len(a)):
        c.append(a[i]+b[i])
    print(c)
    print("***********************************")
    
    
    "27"
    # Cuando juegas a juegos en los que tienes que tirar dos dados, 
    # esbueno conocer las probabilidades de cada tirada. Por ejemplo,
    # las probabilidades de sacar un12son aproximadamente del3%y las 
    # probabilidades de sacar un 7 son de aproximadamente el17%. Puede 
    # calcularlos matemáticamente, pero si no sabe lasmatemáticas, puede 
    # escribir un programa para hacerlo. Parahacer esto, su programa debe 
    # simular el lanzamiento de dos dados unas10,000veces y calcular e
    # imprimir el porcentaje delanzamientos que resultan ser2,3,4,...,12.

    
    a=[]
    b=[]
    c=[]
    for i in range(10000):
        a.append(r.randint(1,6))
        b.append(r.randint(1,6))
        c.append(a[i]+b[i])
            
    print("Si se lanzan dos dados: ")
    for i  in range(2,13):
        prob=(c.count(i)/(len(c)))*100
        print( "la probabilidad que caiga {0} es de {1} porciento".format(i,prob))
    print("***********************************")
    
    
    "28"
    # Usando un bucle for, cree la lista a continuación, que consisteen unos separados 
    # por cada vez más ceros. Los dos últimos dela lista deben estar separados por
    # diez ceros[1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,...]
    
    
    a=[]
    n=-1
    for i in range(11):
        a.append(1)
        n=n+1
        for i in range(n):
            a.append(0)
            
    print(a)
    print("***********************************")
    
    
    
    
    
    #CALCULADORA DE MATRICES 
    
    print("***********************************")
    print("******CALCULADORA DE MATRICES******")
    print("***********************************")
    print("Introduzca matriz A:")
    
    fil=eval(input("Indique número de filas: "))
    col=eval(input("Indique número de columnas: "))
    print("***********************************")
    acum=crea_matriz(fil,col)
    print("***********************************")
    print("\n Matriz A")
    print(acum,"\n")
    print("***********************************")  
    p=input(" LISTA DE OPERACIÓNES\n (+) suma de A y B\n (-) resta de A y B\n (*) producto entre A y B\n (vv) valores y vectores propios \n (x) AX=B  ")
    
    if p=="+":
        print("***********************************")
        print("Matriz B")
        print("***********************************")
        fil2=eval(input("Indique número de filas: "))
        col2=eval(input("Indique número de columnas: "))
        acum2=crea_matriz(fil2,col2)
        print("***********************************")
        print("\n Matriz B")
        print(acum2,"\n")
        print("***********************************")
        print("Resultado:\n",  np.array(acum2)+np.array(acum))
        print("***********************************")
    elif p=="-":
        print("***********************************")
        print("Matriz B")
        print("***********************************")
        fil2=eval(input("Indique número de filas: "))
        col2=eval(input("Indique número de columnas: "))
        print("***********************************")
        acum2=crea_matriz(fil2,col2)
        print("\n Matriz B")
        print(acum2,"\n")
        print("***********************************")
        print("Resultado:\n",  np.array(acum2)-np.array(acum))
        print("***********************************")
        
    elif p=="*":
        print("***********************************")
        print("Matriz B")
        print("***********************************")
        fil2=eval(input("Indique número de filas: "))
        col2=eval(input("Indique número de columnas: "))
        acum2=crea_matriz(fil2,col2)
        print("\n Matriz B")
        print(acum2,"\n")
        print("***********************************")
        print("Resultado:\n",  np.dot(acum2,acum)) 
        print("***********************************")
        
    elif p=="vv":
        print("***********************************")
        print("Valores y vectores propios")
        print("***********************************")
        e_val, e_vec = LA.eig(acum)
        print("valor propio:\n ",e_val )
        print("vector propio:\n ",e_vec )
        print("***********************************")
        
    elif p=="x":
        print("***********************************")
        print("Sistema de la forma AX=B")
        print("***********************************")
        print("Introduzca matriz B")
        fil2=eval(input("Indique número de filas: "))
        col2=eval(input("Indique número de columnas: "))
        print("***********************************")
        acum2=crea_matriz(fil2,col2)
        print("\n Matriz B")
        print(acum2,"\n")
        print("***********************************")
        print("Resultado de X:\n",   np.linalg.inv(acum).dot(acum2))
        print("***********************************")




    #Graficos requeridos

     
    x = np.random.randint(0,10,size=100)
    y = np.random.randint(-20,20,size=100)
    z = np.random.randint(0,30,size=100)
     
    fig = plt.figure()
     
    axes3d = Axes3D(fig)

    axes3d.scatter(x,y,z)
    plt.savefig("a.jpg")



    x = np.linspace(0,20,1000)
     
    y = np.sin(x)
    z = np.cos(x)
     
    fig = plt.figure(figsize=(8,6))
 
    axes3d = Axes3D(fig)
     
    axes3d.plot(x,y,z)
     
    plt.xlabel('X',size = 30)
    plt.ylabel('Y',size = 30)
    axes3d.set_zlabel('Z',color = 'r',size=30)
     
    axes3d.set_yticks([-1,0,1])
    axes3d.set_yticklabels(['min',0,'max'])
    plt.savefig("b.jpg")    

    
    
    fig = plt.figure(figsize=(12,9))
     
    axes3d = Axes3D(fig)
     
     
    zs = [1,5,10,15,20]
     
    for z in zs:
        x = np.arange(0,10)
        y = np.random.randint(0,30,size =10)
        axes3d.bar(x,y,zs = z,zdir = 'x',color=['r','green','yellow','purple'])
    
    plt.savefig("c.jpg")
    
    
    fig = plt.figure()
     
    axes3d = Axes3D(fig)
    
    x = np.linspace(-10,10,100)
    y = np.linspace(-10,10,100)
     
    X,Y = np.meshgrid(x,y)
    Z = np.sqrt(X**2+Y**2)
     
    axes3d.plot_surface(X,Y,Z)
    plt.savefig("d.jpg")

    fig = plt.figure()
    ax = Axes3D(fig)
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')

    plt.savefig("e.jpg")
    
    
    fig, ax = plt.subplots(2, 2, 
                       gridspec_kw={
                           'width_ratios': [3, 2],
                           'height_ratios': [3, 1]})
    
    xa=np.linspace(0,1)
    xb=np.logspace(0,1)
    x = np.linspace(-10*np.pi,10*np.pi,1000)
    
    
    ax[0][0].plot(np.sinc(x), "y")
    ax[0][1].plot(np.log(xa), "m")
    ax[1][0].plot(np.exp(xb), "k-.")
    ax[1][1].plot(range(5), range(10, 5, -1), "r--")

    plt.show()


else:
    print("Hola mundo")


 

    

    
    
    
    
    
    
    
    
    
    
    
    
    