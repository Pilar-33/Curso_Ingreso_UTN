from os import system
system('cls')
'''TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitido
'''
carga_registrar = "si"
flag_mas_votos = True
flag_menos_votos = True
suma_edades = 0
suma_votos = 0
cantidad_candidatos = 0

while carga_registrar == "si":
    nombre = input("Nombre: ")
    
    edad =int(input("Edad: "))
    while edad < 26:
        edad =int(input("Edad (mayor a 25): "))
    
    cantidad_votos = int(input("Votos: "))
    while cantidad_votos < 0:
        cantidad_votos = int(input("Votos (no menor a cero): "))
    
    if flag_mas_votos == True:
        flag_mas_votos = False
        mas_votos = cantidad_votos
        nombre_mas_votos = nombre
    elif cantidad_votos > mas_votos:
        mas_votos = cantidad_votos
        nombre_mas_votos = nombre
    
    if flag_menos_votos == True:
        flag_menos_votos = False
        menos_votos = cantidad_votos
        nombre_menos_votos = nombre
        edad_menos_voto = edad
    elif cantidad_votos < menos_votos:
        menos_votos = cantidad_votos
        nombre_menos_votos = nombre
        edad_menos_voto = edad

    suma_votos += cantidad_votos
    suma_edades += edad
    cantidad_candidatos += 1
    carga_registrar = input("Registra otro candidato (si/no): ")

promedio_edades = suma_edades / cantidad_candidatos
msje = f"                         INFPRME DE CANDIDATOS\n"
msje += f"===================================================================\n"
msje += f"a. nombre del candidato con más votos: {nombre_mas_votos}\n"
msje += f"b. nombre y edad del candidato con menos votos: {nombre_menos_votos}||{edad_menos_voto}\n"
msje += f"c. el promedio de edades de los candidatos: {promedio_edades}\n"
msje += f"d. total de votos emitido: {suma_votos}\n"
print(msje)