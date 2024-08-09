from os import system
system("cls")
"""La municipalidad de la ciudad está realizando un estudio de mercado para determinar cuál
será la nueva actividad recreativa que se difundirá. Las posibles actividades son las
siguientes: Clases de Yoga, Cine al Aire Libre, Taller de Pintura.
Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el
propósito de conocer cuáles son las preferencias de los encuestados (no se sabe cuántos):
Se ingresa de cada encuestado:
● Nombre
● Edad (no menor a 18)
● Está jubilado (si-no)
● Género (Masculino - Femenino - Otro)
● Voto (YOGA, CINE, PINTURA)
Se necesita saber:
1. Cantidad de encuestados no jubilados que votaron por CINE o PINTURA, cuya edad
esté entre 25 y 50 años inclusive.
2. Nombre y voto del encuestado de género Masculino con menor edad.
3. Porcentaje de votos de cada género.
4. Promedio de edad de los encuestados de género Femenino que votaron PINTURA.
5. Determinar cuál fue el género que tuvo más encuestados. """

carga_encuestados = "si"
cantidad_encuestados_no_jubilados_cine_pintura = 0
flag_masculino_menor = True
cantidad_encuestados = 0
voto_masculino = 0
voto_femenino = 0
voto_otro = 0
cantidad_femenino_pintura = 0
edad_femenino_pintura = 0


while carga_encuestados == "si":
    nombre = input("Ingrese su nombre: ")

    edad = int(input("Ingrese su edad: "))
    while edad < 18:
        edad = int(input("Inválida!!!. Ingrese edad (mayor o igual a 18): "))

    estado_jubilado = input("Esta jubilado (si/no)?: ")
    while estado_jubilado != "si" and estado_jubilado != "no":
        estado_jubilado = input("Inválida!!!. Ingrese estado jubilado (si/no): ")

    genero = input("Género (Masculino/Femenino/Otro): ")

    voto = input("Voto (YOGA/CINE/PINTURA): ")
    while voto != "YOGA" and voto != "CINE" and voto != "PINTURA":
        voto = input("Inválida!!!. Ingrese voto (YOGA/CINE/PINTURA): ")

    # 1. Cantidad de encuestados no jubilados que votaron por CINE o PINTURA, cuya edad
    # esté entre 25 y 50 años inclusive.
    if estado_jubilado == "no":
        if voto == "CINE" or voto == "PINTURA":
            if edad > 24 and edad < 51:
                cantidad_encuestados_no_jubilados_cine_pintura += 1

    # 2. Nombre y voto del encuestado de género Masculino con menor edad.
    if genero == "Masculino":
        voto_masculino += 1
        if flag_masculino_menor == True:
            flag_masculino_menor = False
            edad_masculino_menor = edad
            nombre_masculino_menor = nombre
            voto_masculino_menor = voto
        elif edad < edad_masculino_menor:
            edad_masculino_menor = edad
            nombre_masculino_menor = nombre
            voto_masculino_menor = voto
    elif genero == "Femenino":
        voto_femenino += 1
        # 4. Promedio de edad de los encuestados de género Femenino que votaron PINTURA.
        if voto == "PINTURA":
            edad_femenino_pintura += edad
            cantidad_femenino_pintura += 1
    elif genero == "Otro":
        voto_otro += 1

    cantidad_encuestados += 1
    carga_encuestados = input("Ingresar otro voto electrónico (si/no)?: ")
    while carga_encuestados != "si" and carga_encuestados != "no":
        carga_encuestados = input("Inválida!!!. Ingrese carga encuestados (si/no): ")

# 3. Porcentaje de votos de cada género.
porcentaje_masculino = (voto_masculino * 100) / cantidad_encuestados
porcentaje_femenino = (voto_femenino * 100) / cantidad_encuestados
porcentaje_otro = (voto_otro * 100) / cantidad_encuestados

# 4. Promedio de edad de los encuestados de género Femenino que votaron PINTURA.
if cantidad_femenino_pintura != 0:
    promedio_edad_femenino_pintura = edad_femenino_pintura / cantidad_femenino_pintura
else:
    promedio_edad_femenino_pintura = 0

# 5. Determinar cuál fue el género que tuvo más encuestados.

if voto_masculino > voto_femenino and voto_masculino > voto_otro:
    genero_mas_encuestados = "Masculino"
elif voto_femenino > voto_masculino and voto_femenino > voto_otro:
    genero_mas_encuestados = "Femenino"
else:
    genero_mas_encuestados = "Otro"

msje = f""" 
1.  Cantidad de encuestados no jubilados que votaron por CINE o PINTURA, cuya edad
    esté entre 25 y 50 años: {cantidad_encuestados_no_jubilados_cine_pintura}
2.  Nombre y voto del encuestado de género Masculino con menor edad: 
        Nombre: {nombre_masculino_menor}
        Voto: {voto_masculino_menor}
3.  Porcentaje de votos de cada género:
        Masculino: {porcentaje_masculino:.2f}%
        Femenino: {porcentaje_femenino:.2f}%
        Otro: {porcentaje_otro:.2f}%
4.  Promedio de edad de los encuestados de género Femenino que votaron PINTURA: {promedio_edad_femenino_pintura:.2f}%
5.  Género que tuvo más encuestados: {genero_mas_encuestados}
"""
print(msje)
