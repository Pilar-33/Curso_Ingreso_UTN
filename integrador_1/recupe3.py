from os import system
system('cls')
'''Para el hospital Universitario Princeton-Plainsboro de Nueva Jersey.
 Es necesario registrar el ingreso de las mascotas en la próxima hora (solo se pueden
 atender 15 mascotas), para esto hay que considerar los siguientes datos y
 encasillarlos en ciertos diagnósticos para poder derivarlos adecuadamente:
 ● Edad(Validar entre 1 y 20 años)
 ● Tipo: (Validar “gato”, “perro”, “hámster”)
 ● Peso:(Másde0kg)
 ● Diagnóstico: (Validar “problemas digestivos”, “parásitos”, “infección”)
 ● Vacunaantirrábica (validar “si”, ”no”)
 TemaC
 1. Cantidad de mascotas con parásitos o infección, cuya edad se encuentre entre
 los 15 y 18 años con másde15kgdepeso.
 2. El diagnostico mas ingresado de mascotas tipo perro.
 3. Tipo y vacuna de la mascota más menos pesada, cuyo diagnóstico sea
 problemas digestivos.
 4. Porcentaje de mascotas que ingresaron por cada uno de los diagnósticos.
 5. Promedio de edad de los hámster'''

carga_mascota = 0
limite_mascota = 15
cantidad_p_i = 0
cantidad_perro_p_d = 0
cantidad_perro_i = 0
cantidad_perro_p = 0
cantidad_digestivos = 0
cantidad_parasitos = 0
cantidad_infeccion = 0
flag_mascota_pesada = 0
suma_edad_h = 0
cantidad_h = 0


while carga_mascota < limite_mascota:
    print(f"Mascota nro {carga_mascota+1}: ")
    edad = int(input("Edad: "))
    while edad < 1 or edad > 20:
        edad = int(input("Edad incorrecta, ingrese una edad entre 1 y 20 años: "))
    
    tipo = input("Tipo (gato, perro, hamster): ")
    while tipo!= "gato" and tipo!= "perro" and tipo!= "hamster":
        tipo = input("Tipo incorrecto, ingrese un tipo válido (gato, perro, hamster): ")
    
    peso = float(input("Peso: "))
    while peso < 1:
        peso = float(input("Peso incorrecto, ingrese un peso mayor a cero: "))
    
    diagnostico = input("Diagnóstico (problemas digestivos/parasitos/infeccion): ")
    while diagnostico!= "problemas digestivos" and diagnostico!= "parasitos" and diagnostico!= "infeccion":
        diagnostico = input("Diagnóstico incorrecto, ingrese un diagnóstico válido (problemas digestivos/parasitos/infeccion): ")
    
    vacuna = input("Vacuna antirrábica (si/no): ")
    while vacuna!= "si" and vacuna!= "no":
        vacuna = input("Vacuna incorrecta, ingrese si o no: ")
    
    #1. Cantidad de mascotas con parásitos o infección, cuya edad se encuentre entre los 15 y 18 años con más de 15kg de peso
    if (diagnostico == "parasitos" or diagnostico == "infeccion") and ( edad > 14 and edad < 19) and peso > 15:
        cantidad_p_i += 1
    
    #2. El diagnostico mas ingresado de mascotas tipo perro.
    if tipo == "perro":
        if diagnostico == "problemas digestivos":
            cantidad_perro_p_d += 1
        elif diagnostico == "parasitos":
            cantidad_perro_p += 1
        elif diagnostico == "infeccion":
            cantidad_perro_i += 1
    elif tipo == "hamster":
        suma_edad_h += edad
        cantidad_h += 1


    if diagnostico == "problemas digestivos":
        cantidad_digestivos += 1
        if flag_mascota_pesada == True:
            flag_mascota_pesada = False
            peso_mas_pesado = peso
            tipo_mas_pesado = tipo
            vacuna_mas_pesado = vacuna
        elif peso > peso_mas_pesado:
            peso_mas_pesado = peso
            tipo_mas_pesado = tipo
            vacuna_mas_pesado = vacuna
    elif diagnostico == "parasitos":
        cantidad_parasitos += 1
    elif diagnostico == "infeccion":
        cantidad_infeccion += 1    

    carga_mascota += 1

if cantidad_perro_i > cantidad_perro_p and  cantidad_perro_i > cantidad_perro_p_d:
    diagnostico_mas_perro = "infeccion"
elif cantidad_perro_p > cantidad_perro_p_d and cantidad_perro_p > cantidad_perro_i:
    diagnostico_mas_perro = "parasitos"
else:
    diagnostico_mas_perro = "problemas digestivos"


porcentaje_digestivos = (cantidad_digestivos * 100)/carga_mascota
porcentaje_parasitos = (cantidad_parasitos * 100)/carga_mascota
pocentaje_infeccion = (cantidad_infeccion * 100)/carga_mascota

if cantidad_h != 0:
    promedio_hamster = suma_edad_h/cantidad_h
else:
    promedio_hamster = 0

if cantidad_p_i != 0:
    msje = f"1. Cantidad de mascotas con parásitos o infección, cuya edad se encuentre entre los 15 y 18 años con más de 15kg de peso: {cantidad_p_i}\n"
else:
    msje = f"1. Cantidad de mascotas con parásitos o infección, cuya edad se encuentre entre los 15 y 18 años con más de 15kg de peso: Mo hay mascotas\n"

msje += f"2. El diagnostico mas ingresado de mascotas tipo perro: {diagnostico_mas_perro}\n"
msje += f"3. Tipo y vacuna de la mascota más menos pesada, cuyo diagnóstico sea problemas digestivos:\nTipo: {tipo_mas_pesado}\nVacuna: {vacuna_mas_pesado}\n"
msje += f"4. Porcentaje de mascotas que ingresaron por cada uno de los diagnósticos:\nProblemas digestivos: {porcentaje_digestivos}%\nParásitos: {porcentaje_parasitos}%\nInfección: {pocentaje_infeccion}%\n"
msje += f"5. Promedio de edad de los hámster: {promedio_hamster}"