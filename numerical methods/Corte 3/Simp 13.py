# Integración: Regla Simpson 1/3
# Validar cantidad de tramos pares
import numpy as np
import matplotlib.pyplot as plt

# INGRESO
fx = lambda x: np.sqrt(x)*np.sin(x)

# intervalo de integración
a = 1
b = 3
tramos = 8

# Validar cantidad de tramos pares
esimpar = tramos%2
while (esimpar == 1):
    tramos = int(input('tramos es par: '))
    esimpar = tramos%2

# PROCEDIMIENTO
# Regla de Simpson 1/3, varios tramos
h = (b-a)/tramos
xi = a
# segmento por cada dos tramos
suma = fx(xi)
for i in range(0,tramos-2,2):
    xi = xi + h
    suma = suma + 4*fx(xi)
    xi = xi + h
    suma = suma + 2*fx(xi)
# último segmento
xi = xi + h
suma = suma + 4*fx(xi)
suma = suma + fx(b)
area = (h/3)*suma

# SALIDA
print('tramos: ', tramos)
print('Integral: ', area)