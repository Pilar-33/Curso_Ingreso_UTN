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
1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y
25 o entre 36 y 49 o que votaron por IKEA.
2. Nombre y género del encuestado de menor edad que votó por APPLE.
3. Porcentaje de encuestados de género Femenino que votaron por IKEA con
edad mayor a 25 años.
4. Edad promedio de los encuestados que están o no empleados (de cada
uno).
5. Determinar cuál fue la franquicia más votada.'''

carga_voto= "si"
contador_m_v_i  = 0
contador_f_v_i = 0
cantidad_v_f = 0
suma_n_e = 0
cantidad_n_e = 0
cantidad_e = 0
suma_e = 0 
voto_a = 0
voto_d = 0
voto_i = 0
flag_menor_a = True

while carga_voto == "si":
    nombre = input("Ingrese su nombre: ")

    edad = int(input("Edad: "))
    while edad < 18:
        edad = int(input("Edad (debe ser mayor o igual a 18): "))

    esta_empleado = input("Está empleado (si/no): ")
    while esta_empleado != "si" and esta_empleado != "no":
        esta_empleado = input("Error. Está empleado (si/no): ")

    genero = input("Género (M/F/O): ")
    while genero != "F" and genero != "M" and genero != "O":
        genero = input("Error. Género (M/F/O): ")

    voto = input("Voto (APPLE/DUNKIN/IKEA): ")
    while voto != "APPLE" and voto != "DUNKIN" and voto != "IKEA":
        voto = input("Error. Voto (APPLE/DUNKIN/IKEA): ")
    
    #1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y
    #25 o entre 36 y 49 o que votaron por IKEA.
    if genero == "M":
        if (edad > 17 and edad < 26)  or (edad > 35 and edad < 50) or voto == "IKEA":
            contador_m_v_i += 1
    elif genero == "F":
        cantidad_v_f +=1
        if edad > 25 and voto == "IKEA":
            contador_f_v_i += 1
    #2. Nombre y género del encuestado de menor edad que votó por APPLE.
    if voto == "APPLE":
        voto_a +=1
        if flag_menor_a == True:
            flag_menor_a = False
            menor_edad = edad
            menor_nombre = nombre
            menor_genero = genero
        elif edad < menor_edad:
            menor_edad = edad
            menor_nombre = nombre
            menor_genero = genero
    elif voto == "IKEA":
        voto_i +=1
    else:
        voto_d +=1

    if esta_empleado == "no":
        suma_n_e += edad
        cantidad_n_e += 1
    else:
        suma_e += edad
        cantidad_e += 1

    carga_voto = input("Oro voto (si/no): ")

if cantidad_v_f != 0:
    porcentaje_f_i = (contador_f_v_i * 100)/cantidad_v_f
else:
    porcentaje_f_i = 0

if cantidad_n_e != 0:
    edad_promedio_n_e = suma_n_e / cantidad_n_e
else:
    edad_promedio_n_e = 0

if cantidad_e != 0:
    edad_promedio_e = suma_e / cantidad_e
else:
    edad_promedio_e = 0

franquicia_mas_votada = "DUNKIN" 
if voto_a > voto_d and voto_a > voto_i:
    franquicia_mas_votada = "Apple"
elif voto_i > voto_a and voto_i > voto_d:
    franquicia_mas_votada = "IKEA" 

msje = f"1. Cantidad de encuestados de género Masculino, edad esté entre 18 y 25 o entre 36 y 49 o que votaron por IKEA: {contador_m_v_i}\n"

if voto_a > 0: 
    msje += f"2. Nombre y género del encuestado de menor edad que votó por APPLE: {menor_nombre}||{menor_genero}\n"
else:
    msje += f"2. Nombre y género del encuestado de menor edad que votó por APPLE: No hay encuestados que votaron por APPLE.\n"

msje += f"3. Porcentaje de encuestados de género Femenino que votaron por IKEA con edad mayor a 25 años: {porcentaje_f_i}%\n"

msje += f"4. Edad promedio de los encuestados que están o no empleados (de cada uno):\nEdad promedio empleados: {int(edad_promedio_e)} años\nEdad promedio no empleados: {int(edad_promedio_n_e)} años\n"
msje += f"5. Determinar cuál fue la franquicia más votada: {franquicia_mas_votada}"

print(msje)