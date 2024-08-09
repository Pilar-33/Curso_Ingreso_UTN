from os import system
system('cls')
'''UTN Inversiones, realiza un estudio de mercado para saber cuál será la nueva
franquicia que se insertará en el mercado argentino y en la cual invertirán.
Las posibles franquicias son las siguientes: Apple, Dunkin o Ikea.
Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el
propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
Se ingresa de cada encuestado:
● nombre
● edad (no menor a 18)
● está empleado (si-no)
● género (Masculino - Femenino - Otro)
● voto (APPLE, DUNKIN, IKEA)
Se necesita saber:
1. Cantidad de encuestados empleados que votaron por IKEA o APPLE, cuya
edad no supere los 36 años.
2. Nombre y voto del encuestado de género Femenino con mayor edad.
3. Porcentaje de encuestados de género Otro que votaron por DUNKIN.
4. Edad promedio de cada género.
5. Determinar cuál fue el género que tuvo menos encuestados.'''
carga_encuestados = "si"
cantidad_i_a = 0
cantidad_o_d = 0
cantidad_f = 0
cantidad_m = 0
cantidad_o = 0
edad_f = 0
edad_m = 0
edad_o = 0
flag_mayor = True

while carga_encuestados == "si":
    nombre = input("Nombre: ")

    edad = int(input("Edad: "))
    while edad < 18:
        edad = int(input("Edad (no menor a 18): "))
    
    empleado = input("Empleado (si/no): ")
    while empleado != "si" and empleado != "no":
        empleado = input("Error!! .Empleado (si/no): ")
    
    genero = input("Genero (m/f/o): ")
    while genero!= "m" and genero!= "f" and genero!= "o":
        genero = input("Error!!. Genero (m/f/o): ")
    
    voto = input("Voto (APPLE, DUNKIN, IKEA): ")
    while voto !="APPLE" and  voto !="DUNKIN" and voto !="IKEA":
        voto = input("Error!!. Voto (APPLE, DUNKIN, IKEA): ")
    
    if (voto == "IKEA" or voto == "APPLE") and edad < 37:
        cantidad_i_a += 1

    if genero == "f":
        cantidad_f += 1
        edad_f += edad
        if flag_mayor == True:
            flag_mayor = False
            edad_mayor = edad
            nombre_mayor = nombre
            voto_mayor = voto       
        elif edad > edad_mayor:
            edad_mayor = edad
            nombre_mayor = nombre
            voto_mayor = voto   
    elif genero == "o":   
        cantidad_o += 1
        edad_o += edad
        if voto == "DUNKIN":
            cantidad_o_d += 1
    else:
        cantidad_m += 1
        edad_m += edad

    carga_encuestados = input("Carga otro encuestado (si/no): ")

porcentaje_o_d = (cantidad_o_d * 100) / cantidad_o

if cantidad_f != 0:
    promedio_f = edad_f / cantidad_f
else:
    promedio_f = "No se encontraron personas de género femenino"

if cantidad_m != 0:
    promedio_m = edad_m / cantidad_m
else:
    promedio_m = "No se encontraron personas de género masculino"

if cantidad_o != 0:
    promedio_o = edad_o / cantidad_o
else: 
    promedio_o = "No se encontraron personas de género Otro"

genero_menos = "Otro"
if cantidad_f < cantidad_m and cantidad_f < cantidad_o:
    genero_menos = "Femenino"
elif cantidad_m < cantidad_o and cantidad_m < cantidad_f:
    genero_menos = "Masculino"

msje = f"=============================================================================================\n"
msje += f"1. Cantidad de encuestados empleados que votaron por IKEA o APPLE, cuya edad no supere los 36 años: {cantidad_i_a}\n"
if cantidad_f > 0:
    msje += f"2. Nombre y voto del encuestado de género Femenino con mayor edad: {nombre_mayor}||{voto_mayor}\n"
else:
    msje += f"2. Nombre y voto del encuestado de género Femenino con mayor edad: No se encuetaron personas de género Femenino\n"
msje += f"3. Porcentaje de encuestados de género Otro que votaron por DUNKIN: {porcentaje_o_d}%\n"
msje += f"4. Edad promedio de cada género:\nFemenino: {promedio_f}\nMasculino: {promedio_m}\nOtro: {promedio_o}\n"
msje += f"5. Determinar cuál fue el género que tuvo menos encuestados: {genero_menos}"

print(msje)