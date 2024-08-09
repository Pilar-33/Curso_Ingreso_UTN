from os import system
system('cls')

'''
El profesor OAK de pueblo paleta quiere que construyas un segundo modelo prototipico 
de pokedex con 10 pokemones de prueba.

Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon.
    * El tipo de color (azul , amarillo, blanco , otro).
    * La altura del pokemon en centimetros (validar que sea mayor a 10 y menor a 200).

Consignas
    #! 0) - Cantidad de pokemones de color amarillo.
    #! 1) - Cantidad de pokemones de color blanco.
    #! 2) - Nombre, color y altura del pokemon mas alto.
    #! 3) - Nombre, color y altura del pokemon mas bajo.
    #! 4) - Cantidad de pokemones con mas de 100 cm de altura.
    #! 5) - Cantidad de pokemones con menos de 100 cm de altura.
    #! 6) - color de los pokemones del color que mas pokemones posea.
    #! 7) - color de los pokemones del color que menos pokemones posea.
    #! 8) - el promedio de altura de todos los pokemones ingresados.
    #! 9) - el promedio de altura de todos los pokemones azules.
'''
pokemones_amarillo = 0
pokemones_blanco = 0
pokemones_azul = 0
pokemones_otro = 0
cantidad_mas_100 = 0
cantidad_menos_100 = 0
cantidad_pokemones = 0
suma_altura = 0
suma_altura_azules = 0
flag_alto = True
flag_bajo = True

print("Cargando Pokedex...")
while cantidad_pokemones < 11:
    nombre = input("Nombre del pokemon: ")

    color = input("Color del pokemon (amarillo, azul, blanco, otro): ")
    while color != "amarillo" and color != "azul" and color != "blanco" and color != "otro":
        color = input("Inválido!!!. Color del pokemon (amarillo, azul, blanco, otro): ")

    altura = float(input(" Altura del pokemon en cm (10-200): "))
    while altura < 11 or  altura > 200:
        altura = float(input("Inválido. Altura del pokemon en cm (10-200): "))
    
    if color == "amarillo":
        pokemones_amarillo += 1
    elif color == "blanco":
        pokemones_blanco += 1
    elif color  == "azul":
        pokemones_azul += 1
    else:
        pokemones_otro += 1


    if flag_alto == True:
        flag_alto = False
        nombre_alto = nombre
        altura_alto = altura
        color_alto = color
    elif altura > altura_alto:
        nombre_alto = nombre
        altura_alto = altura
        color_alto = color

    if flag_bajo == True:
        flag_bajo = False
        nombre_bajo = nombre
        altura_bajo = altura
        color_bajo = color
    elif altura < altura_bajo:
        nombre_bajo = nombre
        altura_bajo = altura
        color_bajo = color

    if altura > 100:
        cantidad_mas_100 += 1
    else:
        cantidad_menos_100 += 1 

    suma_altura += altura
    cantidad_pokemones += 1

if pokemones_amarillo > pokemones_azul and pokemones_amarillo > pokemones_blanco and pokemones_amarillo > pokemones_otro:
    color_mas_operado = "amarillo"
elif pokemones_blanco > pokemones_amarillo and  pokemones_blanco > pokemones_azul and pokemones_blanco > pokemones_otro:
    color_mas_operado = "blanco"
elif pokemones_azul > pokemones_amarillo and pokemones_azul > pokemones_blanco and pokemones_azul > pokemones_otro:
    color_mas_operado = "azul"
else:
    color_mas_operado = "otro"

if pokemones_amarillo < pokemones_azul and pokemones_amarillo < pokemones_blanco and pokemones_amarillo < pokemones_otro:
    color_menos_operado = "amarillo"
elif pokemones_blanco < pokemones_amarillo and  pokemones_blanco < pokemones_azul and pokemones_blanco < pokemones_otro:
    color_menos_operado = "blanco"
elif pokemones_azul < pokemones_amarillo and pokemones_azul < pokemones_blanco and pokemones_azul < pokemones_otro:
    color_menos_operado = "azul"
else:
    color_menos_operado = "otro"

promedio_altura = suma_altura / cantidad_pokemones

if pokemones_azul > 0:
    promedio_altura_azules = suma_altura_azules / pokemones_azul
else:
    promedio_altura_azules = "No hay pokemones azules"

msje = f"0) - Cantidad de pokemones de color amarillo: {pokemones_amarillo}\n"
msje += f"1) - Cantidad de pokemones de color blanco: {pokemones_blanco}\n"
msje += f"2) - Nombre, color y altura del pokemon mas alto: {nombre_alto}|| {color_alto}||{altura_alto}\n"
msje += f"3) - Nombre, color y altura del pokemon mas bajo: {nombre_bajo}|| {color_bajo}||{altura_bajo}\n"
msje += f"4) - Cantidad de pokemones con mas de 100 cm de altura: {cantidad_mas_100}\n"
msje += f"5) - Cantidad de pokemones con menos de 100 cm de altura: {cantidad_menos_100}\n"
msje += f"6) - color de los pokemones del color que mas pokemones posea: {color_menos_operado}\n"
msje += f"7) - color de los pokemones del color que menos pokemones posea: {color_mas_operado}\n"
msje += f"8) - el promedio de altura de todos los pokemones ingresados: {promedio_altura}\n"
msje += f"9) - el promedio de altura de todos los pokemones azules: {promedio_altura_azules}\n"

print(msje)