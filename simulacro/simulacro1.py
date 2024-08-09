from os import system
system("cls")
"""
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
menor_masculino = -1
msje = ""

while carga_encuestados == "si":
    nombre = input("Nombre: ")

    edad = int(input("Edad: "))
    while edad < 18:
        edad = int(input("Inválida!!!. Ingrese edad (mayor o igual a 18): "))

    estado_jubilado = input("Esta jubilado (si/no)?: ")
    while estado_jubilado != "si" and estado_jubilado != "no":
        estado_jubilado = input("Inválida!!!. Ingrese estado jubilado (si/no): ")

    genero = input("Género (Masculino/Femenino/Otro): ")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input("Inválida!!!. Ingrese género (Masculino/Femenino/Otro): ")

    voto = input("Voto (YOGA/CINE/PINTURA): ")
    while voto != "YOGA" and voto != "CINE" and voto != "PINTURA":
        voto = input("Inválida!!!. Ingrese voto (YOGA/CINE/PINTURA): ")

    if estado_jubilado == "no":
        if voto == "CINE" or voto == "PINTURA":
            if edad > 24 and edad < 51:
                cantidad_encuestados_no_jubilados_cine_pintura += 1

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
        if voto == "PINTURA":
            edad_femenino_pintura += edad
            cantidad_femenino_pintura += 1
    else:
        voto_otro += 1

    cantidad_encuestados += 1
    carga_encuestados = input("Desea ingresar otro voto electrónico (si/no)?: ")
    
porcentaje_masculino = (voto_masculino * 100) / cantidad_encuestados
porcentaje_femenino = (voto_femenino * 100) / cantidad_encuestados
porcentaje_otro = (voto_otro * 100) / cantidad_encuestados


if cantidad_femenino_pintura != 0:
    promedio_edad_femenino_pintura = edad_femenino_pintura / cantidad_femenino_pintura
else:
    promedio_edad_femenino_pintura = 0

genero_mas_encuestados = "Otro"
if voto_masculino > voto_femenino and voto_masculino > voto_otro:
    genero_mas_encuestados = "Masculino"
elif voto_femenino > voto_masculino and voto_femenino > voto_otro:
    genero_mas_encuestados = "Femenino"

msje = f"1. Cantidad de encuestados no jubilados que votaron por CINE o PINTURA, cuya edad esté entre 25 y 50 años: {cantidad_encuestados_no_jubilados_cine_pintura}\n"

if menor_masculino == -1:
        msje += "2. No se ingresó ningún encuestado de género Masculino\n"
else:
    msje += f"2. Nombre y voto del encuestado de género Masculino con menor edad: \nNombre: {nombre_masculino_menor} \nVoto: {voto_masculino_menor}"

msje += f"3.  Porcentaje de votos de cada género: \nMasculino: {porcentaje_masculino:.2f}% \nFemenino: {porcentaje_femenino:.2f}% \nOtro: {porcentaje_otro:.2f}%\n"
msje += f"4.  Promedio de edad de los encuestados de género Femenino que votaron PINTURA: {promedio_edad_femenino_pintura:.2f}%\n"
msje += f"5.  Género que tuvo más encuestados: {genero_mas_encuestados}\n"

print(msje)
