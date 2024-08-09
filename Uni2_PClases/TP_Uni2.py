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

suma_edades = 0
total_votos = 0
contador = 0
flag_votos_mayor = True
#control + k +c
#control + k + u
#control + d

print("=" *35)
print("        While_Reality_Show ")
print("=" * 35)

while contador < 3:
    print(f"Ingrese datos del {contador + 1}° jugador:")
    print("--------------------------------------")
    nombre = input("Nombre: ")
    
    #Validando edad
    edad = int(input("Edad (mayor 25): "))
    
    while edad < 25:
        edad = int(input("Ingrese edad válida, mayor a 25: "))
        
    
    #Validando votos
    votos = int(input("Cantidad de votos (no menor a cero): "))
    
    while votos < 0:
        votos = int(input("Ingrese votos válidos, no menor a cero: "))
        
    
    if flag_votos_mayor == True:
        flag_votos_mayor = False
        max_votos = votos
        min_votos = votos
        max_nombre = nombre
        min_nombre = nombre
        min_edad = edad
    
    if votos > max_votos:
        max_votos = votos
        max_nombre = nombre
    elif votos < min_votos:
        min_votos = votos
        min_nombre = nombre
        min_edad = edad
        
    suma_edades += edad
    total_votos += votos
    contador += 1
    print("")

promedio = suma_edades/contador
msje = f"a. Nombre del candidato con más votos: {max_nombre}\n"
msje += f"b. Nombre y edad del candidato con menos votos: {min_nombre}, {min_edad} años\n"
msje += f"c. Promedio de edades de los candidatos: {promedio:.2f}\n"
msje += f"d. Total de votos emitidos: {total_votos} votos"

print('''INFORME GENERAL: ''' + "\n" + "*"*70 + "\n" + msje)