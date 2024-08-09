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
TemaA
1.Cantidad de mascotas con vacuna antirrábica, cuya edad está entre los 5 y 10
años, que se presentaron por problemas digestivos o parásitos.
2. El tipo de mascota másingresada con problemas digestivos.
3. Edadytipodelamascotamásvieja sin vacuna antirrábica.
4. Porcentaje de mascotas vacunadas y no vacunadas.
5. Promedio de edad de los perros'''

carga_mascotas = 0
limite = 15
cantidad_m_pd_p = 0
cantidad_m_p = 0
cantidad_m_g = 0
cantidad_m_h = 0
mascotas_vacunadas = 0
mascotas_no_vacunadas = 0
suma_edad_p = 0
flag_mas_vieja = True


while carga_mascotas < limite:
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
    
    if vacuna == "si":
        mascotas_vacunadas += 1
        if (edad > 4 and edad < 11) and (diagnostico == "problemas digestivos" or diagnostico == "parasitos"):
            cantidad_m_pd_p += 1
    elif vacuna == "no":
        mascotas_no_vacunadas +=1
        if flag_mas_vieja == True:
            flag_mas_vieja = False
            edad_mas_vieja = edad
            tipo_mas_vieja = tipo
        elif edad < edad_mas_vieja:
            edad_mas_vieja = edad
            tipo_mas_vieja = tipo
        
    if diagnostico == "problemas digestivos":
        if tipo == "gato":
            cantidad_m_g += 1
        elif tipo == "perro":
            cantidad_m_p += 1
            suma_edad_p += edad 
        elif tipo == "hamster":
            cantidad_m_h += 1

    carga_mascotas +=1

if cantidad_m_g > cantidad_m_p and cantidad_m_g > cantidad_m_h:
    mascota_mas_ingresad_pd = "Gato"
elif cantidad_m_p > cantidad_m_g and cantidad_m_p > cantidad_m_h:
    mascota_mas_ingresad_pd = "Perro"
else:
    mascota_mas_ingresad_pd = "Hamster"

#4. Porcentaje de mascotas vacunadas y no vacunadas.
porcentaje_vacunadas = (mascotas_vacunadas * 100)/ carga_mascotas
porcentaje_no_vacunadas = (mascotas_no_vacunadas * 100)/ carga_mascotas

#5. Promedio de edad de los perros
if cantidad_m_p != 0:
    promedio_edad_p = suma_edad_p / cantidad_m_p
else:
    promedio_edad_p = 0

msje = f"1.Cantidad de mascotas con vacuna antirrábica, cuya edad está entre los 5 y 10 años, que se presentaron por problemas digestivos o parásitos: {cantidad_m_pd_p}\n"
msje += f"2. El tipo de mascota más ingresada con problemas digestivos: {mascota_mas_ingresad_pd}\n"
msje += f"3. Edad y tipo de la mascota más vieja sin vacuna antirrábica: {edad_mas_vieja} año(s)||{tipo_mas_vieja}\n"
msje += f"4. Porcentaje de mascotas vacunadas y no vacunadas:\nMascotas vacunadas: {mascotas_vacunadas}%\nMascotas no vacunadas: {mascotas_no_vacunadas}\n"
msje += f"5. Promedio de edad de los perros: {promedio_edad_p}\n"
print(msje)