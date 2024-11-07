# Paso1: solicitar al usuario que ingrese el radio del circulo que quiere calcular


#Paso2:Calcular el area del circulo utilizando la formula del area: π*radio^2



#Paso3: Mostrar al usuario el area calculad



import math


ingresar_radio = float(input('Por favor, ingrese el radio en cm del círculo: '))


area= math.pi*(ingresar_radio**2)

print(f'el area del circulo es:',area,'cm2')