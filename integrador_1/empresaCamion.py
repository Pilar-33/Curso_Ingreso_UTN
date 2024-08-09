from os import system
system('cls')
'''Empresa de Camiones: Para el departamento de logística: 
A. Es necesario saber la cantidad de camiones que harían falta para transportar los materiales que 
se utilizarán para la construcción de un edificio. Para ello, se ingresa la cantidad de toneladas 
necesarias de materiales a transportar. El programa deberá informar la cantidad de camiones, sabiendo 
que cada uno de ellos puede transportar por viaje 3500kg. 
B. A partir del ingreso de la cantidad de kilómetros que tiene que recorrer estos 
camiones para llegar al destino de la obra, necesitamos que el programa informe cual es el 
tiempo (en horas) que tardará cada uno de los camiones, 
si sabemos que cada camión puede ir a una velocidad máxima y constante de 90 km/h.'''
#cantidad de caminones =?
#Parte A
cada_camion_transporta = 3500
cantidad_de_toneladas = float(input("Ingrese cantidad de toneladas a transportar: "))

#convertir a kg
cantidad_de_kg = cantidad_de_toneladas * 1000

#Evaluar cuuantos camiones se necesita
# 1 camion -------> cada_camion_transporta
#   x      -------> cantidad_de_kg  
# x = (1 camion * cantidad_de_kg)/cada_camion_transporta
cantidad_de_camiones = cantidad_de_kg // cada_camion_transporta  
#cantidad_de_camiones = (cantidad_de_kg + cada_camion_transporta - 1) // cada_camion_transporta  # Redondeo hacia arriba
#Parte B
velocidad_maxima_constante = 90
cantidad_kilometros_recorrer = float(input("Ingrese cantidad de Km a recorrer: "))

#hallar tiempo que tarda cada camión
## 1 camion -------> velocidad_maxima_constante
##  x      -------> cantidad_kilometros_recorrer
# x = (1 camion * cantidad_kilometros_recorrer)/velocidad_maxima_constante
tiempo_camion = cantidad_kilometros_recorrer / velocidad_maxima_constante

#mostrar datos
msje = f'''
                        PARTE A
===================================================
cantidad de camiones: {int(cantidad_de_camiones)} camiones
                        PARTE B
====================================================
Tiempo que tarda cada uno de los camiones: {tiempo_camion:.2f} horas'''

print(msje)