from os import system
system('cls')
'''UTN Inversiones, realiza un estudio de mercado para saber cuál será la nueva
 franquicia que se insertará en el mercado argentino y en la cual invertirán.
 Las posibles franquicias son las siguientes: Apple, Dunkin o Ikea.
 Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el
 propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
 Se ingresa de cada encuestado:
 ● nombre
 ● edad(nomenora18)
 ● estáempleado(si-no)
 ● género(Masculino- Femenino- Otro)
 ● voto(APPLE,DUNKIN, IKEA)
 Se necesita saber:
 1.Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA, cuya edad esté entre 25 y 50 años inclusive.
 2. Nombreyvotodelencuestado degéneroMasculino con menor edad.
 3. Porcentaje de votos de cada género.
 4. Promedio de edad de los encuestados de género Femenino que votaron IKEA.
 5. Determinar cuál fue el género que tuvo más encuestados
'''
carga_voto = "si"
cantidad_desempleados_d_i = 0
cantidad_f_i = 0
suma_edad_f_i = 0
cantidad_m = 0
cantidad_f = 0
cantidad_o = 0
cantidad_general = 0
flag_menor_m = True

while carga_voto == "si":
    nombre = input("Nombre: ")

    edad = int(input("Edad: "))
    while edad < 18:
        edad = int(input("Edad (debe ser mayor o igual a 18): "))

    esta_empleado = input("¿Está empleado (si/no)? ")
    while esta_empleado !="si" and esta_empleado != "no":
        esta_empleado = input("Error. ¿Está empleado (si/no)? ")

    genero = input("Ingrese género (M/F/O): ")
    while genero!= "M" and genero!= "F" and genero!= "O":
        genero = input("Error. Género (M/F/O): ")

    voto = input("Ingrese voto (APPLE/DUNKIN/IKEA): ")
    while voto != "APPLE" and voto != "DUNKIN" and voto != "IKEA":
        voto = input("Error. Voto (APPLE/DUNKIN/IKEA): ")
    
    if (esta_empleado == "no") and (voto == "DUNKIN" or voto == "IKEA") and (edad > 24 and edad < 51):
        cantidad_desempleados_d_i += 1

    if genero == 'M':
        cantidad_m += 1
        if flag_menor_m == True:
            flag_menor_m = False
            menor_m_edad = edad
            menor_m_nombre = nombre
            menor_m_voto = voto
        elif edad < menor_m_edad:
            menor_m_edad = edad
            menor_m_nombre = nombre
            menor_m_voto = voto
    elif genero == 'F':
        cantidad_f += 1
        if voto == "IKEA":
            cantidad_f_i += 1
            suma_edad_f_i += edad
    else:
        cantidad_o += 1


    cantidad_general += 1
    carga_voto = input("Carga voto: (si/no): ")

if cantidad_general != 0:
    porcentaje_f = (cantidad_f * 100)/cantidad_general
    porcentaje_m = (cantidad_m * 100)/cantidad_general
    porcentaje_o = (cantidad_o * 100)/cantidad_general
else:
    porcentaje_f = "No hay encuestados de género femenino"
    porcentaje_m = "No hay encuestados de género masculino"
    porcentaje_o = "No hay encuestados de género otro"

if cantidad_f_i!= 0:
    promedio_f_i = suma_edad_f_i/cantidad_f_i
else:
    promedio_f_i = "No hay encuestados de género femenino que votaron IKEA"

mayor_genero = "Otro"
if cantidad_f > cantidad_m and  cantidad_f > cantidad_o:
    mayor_genero = "Femenino"
elif cantidad_m > cantidad_f and cantidad_m > cantidad_o:
    mayor_genero = "Masculino"
    
msje = f"1.Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA, cuya edad esté entre 25 y 50 años inclusive: {cantidad_desempleados_d_i}\n"
if cantidad_m != 0:
    msje += f"2. Nombre y voto del encuestado de género Masculino con menor edad: {menor_m_nombre}||{menor_m_voto}\n"
else:
    msje += "2. Nombre y voto del encuestado de género Masculino con menor edad: No hay encueatdos de género masculino"

msje += f"3. Porcentaje de votos de cada género: \nFemenino: {porcentaje_f}%\nMasculino: {porcentaje_m}%\nOtro: {porcentaje_o}%\n"
msje += f"4. Promedio de edad de los encuestados de género Femenino que votaron IKEA: {promedio_f_i}\n"
msje += f"5. Determinar cuál fue el género que tuvo más encuestados: {mayor_genero}"
print(msje)