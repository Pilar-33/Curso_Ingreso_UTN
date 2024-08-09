from os import system
system('cls')
'''El presentador del torneo de artes marciales quiere que desarrolles un modelo prototipico 
de scouter (un detector basicamente) para ver ciertas metricas de los participantes.
de cualquier parte del universo, es por eso que deberas realizar la carga 
de 10 participantes.
Para ello deberas programar el boton "Cargar Guerreros" para poder cargar 10 Caballeros del zodiaco.
Los datos que deberas pedir para los Caballeros del zodiaco son:
    * El nombre del Caballeros del zodiaco.
    * El tipo de armadura (Bronce, Plata, Oro, Divina, Oscura).
    * La cantidad de cosmos del guerrero (entre 25000 y 150000).
Consignas:
    #! 0) - Cantidad de guerreros de armadura de Oro.
    #! 1) - Cantidad de guerreros de armadura Divina.
    #! 2) - Nombre, Armadura y Cosmos del guerrero mas fuerte.
    # 3) - Nombre, Raza y Poder del guerrero mas debil.
    # 4) - Cantidad de guerreros con mas de 85000 de poder y armadura de Plata.
    # 5) - Cantidad de guerreros con menos de 50000 de poder y armadura de Bronce.
    #! 6) - Armadura que mas guerreros posea inscriptos.
    #! 7) - Armadura que menos guerreros posea inscriptos.
    #! 8) - el promedio de cosmos de todos los guerreros con armadura Oscura.
    #! 9) - el porcentaje, tipo de armadura y promedio de cosmos de guerreros 
    #!      de cada tipo de armadura, respecto al total de guerreros.
'''
carga_guerrero = 0
limite_guerrero = 5
cantidad_armadura_oro = 0
cantidad_armadura_divina = 0
cantidad_armadura_plata = 0
cantidad_armadura_bronce = 0
cantidad_armadura_oscura = 0
suma_oscura = 0
suma_oro = 0
suma_divina = 0
suma_bronce = 0
suma_plata = 0
flag_guerrero_fuerte = True

while carga_guerrero < limite_guerrero:
    nombre = input(f"Nombre del guerrero {carga_guerrero + 1}: ")

    armadura = input(f"Armadura del guerrero {carga_guerrero + 1} (bronce, plata, oro, divina, oscura): ")
    while armadura != "bronce" and armadura != "plata" and armadura != "oro" and armadura != "divina" and armadura != "oscura":
        armadura = input(f"Armadura incorrecta, ingrese armadura válida (bronce, plata, oro, divina, oscura): ")

    cosmos = int(input(f"Cangtidad de cosmos del guerrero {carga_guerrero + 1} (entre 25000 y 150000): "))
    while cosmos < 25000 or cosmos > 150000:
        cosmos = int(input(f"Cantidad de cosmos incorrecta, ingrese cantidad entre 25000 y 150000: "))

    if armadura == "oro":
        cantidad_armadura_oro += 1
        suma_oro += cosmos
    elif armadura == "divina":
        cantidad_armadura_divina += 1
        suma_divina += cosmos
    elif armadura == "plata":
        cantidad_armadura_plata += 1
        suma_plata += cosmos
    elif armadura == "bronce":
        cantidad_armadura_bronce += 1
        suma_bronce += cosmos
    elif armadura == "oscura":   
        cantidad_armadura_oscura += 1
        suma_oscura += cosmos

    if flag_guerrero_fuerte == True:
        flag_guerrero_fuerte = False
        nombre_guerrero_fuerte = nombre
        armadura_fuerte = armadura
        cosmos_fuerte = cosmos
    elif cosmos > cosmos_fuerte:
        nombre_guerrero_fuerte = nombre
        armadura_fuerte = armadura
        cosmos_fuerte = cosmos

    carga_guerrero += 1

if cantidad_armadura_oscura > cantidad_armadura_oro and cantidad_armadura_oscura > cantidad_armadura_divina and cantidad_armadura_oscura > cantidad_armadura_plata and cantidad_armadura_oscura > cantidad_armadura_bronce:
    armadura_mas_guerreros = "Armadura Oscura"
elif cantidad_armadura_plata > cantidad_armadura_bronce and cantidad_armadura_plata > cantidad_armadura_divina and cantidad_armadura_plata > cantidad_armadura_oro and cantidad_armadura_plata > cantidad_armadura_oscura:
    armadura_mas_guerreros = "Armadura Plata"
elif cantidad_armadura_bronce > cantidad_armadura_divina and cantidad_armadura_bronce > cantidad_armadura_oro and cantidad_armadura_bronce > cantidad_armadura_oscura and cantidad_armadura_bronce > cantidad_armadura_plata:
    armadura_mas_guerreros = "Armadura Bronce"
elif cantidad_armadura_divina > cantidad_armadura_oro and cantidad_armadura_divina > cantidad_armadura_bronce and cantidad_armadura_divina > cantidad_armadura_oscura and cantidad_armadura_divina > cantidad_armadura_plata:
    armadura_mas_guerreros = "Armadura Divina"
else:
    armadura_mas_guerreros = "Armadura Oro"

if cantidad_armadura_oscura < cantidad_armadura_oro and cantidad_armadura_oscura < cantidad_armadura_divina and cantidad_armadura_oscura < cantidad_armadura_plata and cantidad_armadura_oscura < cantidad_armadura_bronce:
    armadura_menos_guerreros = "Armadura Oscura"
elif cantidad_armadura_plata < cantidad_armadura_bronce and cantidad_armadura_plata < cantidad_armadura_divina and cantidad_armadura_plata < cantidad_armadura_oro and cantidad_armadura_plata < cantidad_armadura_oscura:
    armadura_menos_guerreros = "Armadura Plata"
elif cantidad_armadura_bronce < cantidad_armadura_divina and cantidad_armadura_bronce < cantidad_armadura_oro and cantidad_armadura_bronce < cantidad_armadura_oscura and cantidad_armadura_bronce < cantidad_armadura_plata:
    armadura_menos_guerreros = "Armadura Bronce"
elif cantidad_armadura_divina < cantidad_armadura_oro and cantidad_armadura_divina < cantidad_armadura_bronce and cantidad_armadura_divina < cantidad_armadura_oscura and cantidad_armadura_divina < cantidad_armadura_plata:
    armadura_menos_guerreros = "Armadura Divina"
else:
    armadura_menos_guerreros = "Armadura Oro"

if cantidad_armadura_oscura != 0:
    promedio_oscuro = suma_oscura/cantidad_armadura_oscura
else:
    promedio_oscuro = 0

if cantidad_armadura_divina != 0:
    promedio_divina = suma_divina/cantidad_armadura_divina
else:
    promedio_divina = 0

if cantidad_armadura_oro != 0:
    promedio_oro = suma_oro/cantidad_armadura_oro
else:
    promedio_oro = 0

if cantidad_armadura_bronce != 0:
    promedio_bronce = suma_bronce/cantidad_armadura_bronce
else:
    promedio_bronce = 0

if cantidad_armadura_plata != 0:
    promedio_plata = suma_plata/cantidad_armadura_plata
else:
    promedio_plata = 0

porcentaje_plata = (cantidad_armadura_plata * 100)/carga_guerrero
porcentaje_bronce = (cantidad_armadura_bronce * 100)/carga_guerrero
porcentaje_oro = (cantidad_armadura_oro *100)/carga_guerrero
porcentaje_oscura = (cantidad_armadura_oscura * 100)/carga_guerrero
porcentaje_divina = (cantidad_armadura_divina * 100)/carga_guerrero


msje = f"0) Cantidad de guerreros de armadura de Oro: {cantidad_armadura_oro}\n"
msje += f"1) Cantidad de guerreros de armadura Divina: {cantidad_armadura_divina}\n"
msje += f"2) Nombre, Armadura y Cosmos del guerrero mas fuerte:\nNombre: {nombre_guerrero_fuerte}\nArmadura: {armadura_fuerte}\nCosmos: {cosmos_fuerte}\n"
msje += f"6) Armadura que mas guerreros posea inscriptos: {armadura_mas_guerreros}\n"
msje += f"7) Armadura que menos guerreros posea inscriptos: {armadura_menos_guerreros}\n"
msje += f"8) Promedio de armadura oscura: {promedio_oscuro}\n"
msje += f"9) El porcentaje, tipo de armadura y promedio de cosmos de guerreros de cada tipo de armadura, respecto al total de guerreros:{porcentaje_bronce}%||{porcentaje_divina}%||{porcentaje_oro}%||{porcentaje_oscura}%||{porcentaje_plata}%\n{promedio_bronce}||{porcentaje_divina}||{promedio_oro}||{promedio_oscuro}||{promedio_plata}\n"

print(msje)