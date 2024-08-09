from os import system
system('cls')
"""TP:  While_Reality_Show
Enunciado:
De los 3 Jugadores de un Reality Show, se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos
Informar:
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan mediante input()"""
contador = 0
flag_max_votos = True
flag_min_votos = True
suma_votos = 0

while contador < 3:
    nombre = input("Nombre: ")
    
    edad = int(input("Edad: "))
    while edad < 26:
        edad = int(input("Edad debe ser mayor a 25: "))
        
    votos = int(input("Votos: "))
    while votos < 0:
        votos = int(input("Inválido, Ingrese cantidad de Votos: "))
        
    if flag_max_votos == True:
        flag_max_votos = False
        max_votos = votos
        nombre_max_votos = nombre
    elif votos > max_votos:
        max_votos = votos
        nombre_max_votos = nombre
    
    if flag_min_votos == True:
        flag_min_votos = False
        min_votos = votos
        nombre_min_votos = nombre
        edad_min_votos = edad
    elif votos < min_votos:
        min_votos = votos
        nombre_min_votos = nombre
        edad_min_votos = edad
    
    suma_votos += votos
    contador += 1

msje = f"a. nombre del candidato con más votos: {nombre_max_votos}\n"
msje += f"b. nombre y edad del candidato con menos votos: {nombre_min_votos}||{edad_min_votos}\n"
msje += f"d. total de votos emitidos: {suma_votos}"

print(msje)