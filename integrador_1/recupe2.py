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
 TemaB
 1.Cantidad de perros o gatos, sin vacuna antirrábica, que pesan entre 10 y 20 kg,
 2. El tipo de mascota másingresada con parásitos.
 3. Edad y diagnóstico de la mascota más joven que se presentaron con una
 infección.
 4. Porcentaje de mascotas de cada tipo.
 5. Promedio de pesos de mascotas con parásitos'''

carga_mascota = 0
limite_mascota = 15
cantidad_no_vacunadas_p_g = 0
cantidad_g_p = 0
cantidad_h_p = 0
cantidad_p_p = 0
cantidad_g = 0
cantidad_p = 0
cantidad_h = 0
suma_peso_p = 0
cantidad_parasito = 0
flag_mascota_joven = True

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
        vacuna = input("Vacuna antirrábica incorrecta, ingrese un valor válido (si/no): ")

    #1.Cantidad de perros o gatos, sin vacuna antirrábica, que pesan entre 10 y 20 kg,
    if vacuna == "no":
        if (tipo == "gato" or tipo == "perro") and (peso > 9 and peso < 21):
            cantidad_no_vacunadas_p_g += 1
    
    #2. El tipo de mascota más ingresada con parásitos.
    if diagnostico == "parasitos":
        cantidad_parasito += 1
        suma_peso_p += peso
        if tipo == "gato":
            cantidad_g_p += 1
        elif tipo == "perro":
            cantidad_p_p += 1
        elif tipo == "hamster":
            cantidad_h_p += 1

    #3. Edad y diagnóstico de la mascota más joven que se presentaron con una infección.
    if flag_mascota_joven == True:
        flag_mascota_joven = False
        edad_mas_joven = edad
        diagnostico_mas_joven = diagnostico
    elif edad < edad_mas_joven:
        edad_mas_joven = edad
        diagnostico_mas_joven = diagnostico

    if tipo == "perro":
        cantidad_p += 1
    elif tipo == "gato":
        cantidad_g += 1
    else:
        cantidad_h += 1
    carga_mascota += 1
    print("")

if cantidad_p_p == cantidad_g_p == cantidad_h_p:
    tipo_mas_ingresada = "gato, perro y hamster"
elif cantidad_g_p == cantidad_h_p:
    tipo_mas_ingresada = "gato y hamster"
elif cantidad_g_p == cantidad_p_p:
    tipo_mas_ingresada = "gato y perro"
elif cantidad_p_p == cantidad_h_p:
    tipo_mas_ingresada = "perro y hamster"

if cantidad_g_p > cantidad_h_p and cantidad_g_p > cantidad_p_p:
    tipo_mas_ingresada = "gato"
if cantidad_p_p > cantidad_h_p and cantidad_p_p > cantidad_g_p:
    tipo_mas_ingresada = "perro"
if cantidad_h_p > cantidad_g_p and cantidad_h_p > cantidad_p_p:
    tipo_mas_ingresada = "hamster"

porcentaje_p = (cantidad_p * 100)/carga_mascota
porcentaje_g = (cantidad_g * 100)/carga_mascota
porcentaje_h = (cantidad_h * 100)/carga_mascota

if cantidad_parasito != 0:
    promedio_peso_p = suma_peso_p / cantidad_parasito
else:
    promedio_peso_p = 0

msje = f"1. Cantidad de perros o gatos, sin vacuna antirrábica, que pesan entre 10 y 20 kg: {cantidad_no_vacunadas_p_g} mascota(s)\n"
msje += f"2. El tipo de mascota más ingresada con parásitos: {tipo_mas_ingresada}\n"
msje += f"3. Edad y diagnóstico de la mascota más joven que se presentaron con una infección: {edad_mas_joven} año(s)||{diagnostico_mas_joven}\n"
msje += f"4. Porcentaje de mascotas de cada tipo:\nPerro: {porcentaje_p}%\nGato: {porcentaje_g}%\nHamster: {porcentaje_h}%\n"
msje += f"5. Promedio de pesos de mascotas con parásitos: {promedio_peso_p} años"

print(msje)