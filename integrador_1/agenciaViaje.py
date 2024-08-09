from os import system
system('cls')

# Agenciadeviaje: Para saber el costo de un viaje necesitamos el siguiente algoritmo, 
#?sabiendo que el precio por kilo de pasajero es 1000 pesos.
#? Se ingresan todos los datos por PROMPT los datos a solicitar de dos personas son: nombre, edad y peso 
# Se pide armar el siguiente mensaje: 
#! "Hola jose y maria , sus pesos son 80 kilos y 60 kilos respectivamente, sumados da 140 kilos , 
#! el promedio de edad es 33 y su viaje vale 140000 pesos "*/

precio_kilo_pasajero = 1000
contador = 0
suma_peso = 0
suma_edad = 0
msje =""

print('''        
            INGRESE DATOS DE DOS PERSONAS
=============================================''')
while contador < 2:
    print(f"Datos persona n°{contador + 1}" + "\n" + "="*45)
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    peso = int(input("Peso (kg): "))
    
    if contador == 0:
        nombre1 = nombre
        peso1 = peso
    else:
        nombre2 = nombre
        peso2 = peso
    suma_peso += peso
    suma_edad += edad
    contador += 1
#============================================
# Cálculos
promedio_edad = suma_edad / 2
costo_viaje = suma_peso * precio_kilo_pasajero
#==============================================
msje = f'''
*************************************************************************************
"Hola {nombre1} y {nombre2} , sus pesos son {peso1} kilos y {peso2} kilos respectivamente, 
sumados da {suma_peso} kilos, el promedio de edad es {promedio_edad} y su viaje vale {costo_viaje} pesos "'''

print(msje)