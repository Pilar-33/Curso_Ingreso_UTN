rta = "si"
contador_no_jubilados = 0
flag_m_mas_joven = True
menor_nombre = "-1"

contador_general = 0
contador_m = 0
contador_f = 0
contador_o = 0

contador_f_pintura = 0
acum_edad_f_pintura = 0

while (rta == "si"):
    nombre = input("Nombre: ")

    edad = int(input("Edad: "))
    while (edad < 18):
        edad = int(input("Edad: "))

    jubilado = input("Jubilado: ")
    while (jubilado != "si" and jubilado != "no"):
        jubilado = input("Jubilado: ")

    sexo = input("Sexo: ")
    while (sexo != "m" and sexo != "f" and sexo != "o"):
        sexo = input("sexo: ")

    voto = input("Voto: ")
    while (voto != "YOGA" and voto != "CINE" and voto != "PINTURA"):
        voto = input("Voto: ")

    contador_general += 1

    if (sexo == "m"):
        contador_m += 1

        if (flag_m_mas_joven == True):
            flag_m_mas_joven = False

            menor_edad = edad

            menor_nombre = nombre
            menor_voto = voto
        elif (edad < menor_edad):
            menor_edad = edad
            menor_nombre = nombre
            menor_voto = voto
    elif (sexo == "f"):
        contador_f += 1

        if (voto == "PINTURA"):
            contador_f_pintura += 1
            acum_edad_f_pintura += edad
    else:
        contador_o += 1

    if (jubilado == "no" and (voto == "CINE" or voto == "PINTURA") and (edad > 24 and edad < 51)):
        contador_no_jubilados += 1

    rta = input("SEGUIR? (si): ")


print(f"Cantidad de encuestados no jubilados que votaron por CINE o PINTURA, cuya edad
    esté entre 25 y 50 años inclusive: {contador_no_jubilados}") 

if (menor_nombre == "-1"):
    print("no se ingresaron hombres")
else:
    print(f"Nombre y voto del encuestado de género Masculino con menor edad: {menor_nombre} || {menor_voto}")

porcentaje_m = contador_m  * 100 / contador_general
porcentaje_f = contador_f  * 100 / contador_general
porcentaje_o = contador_o  * 100 / contador_general
print(f"M: {porcentaje_m}% || F: {porcentaje_f}% || O: {porcentaje_o}%")


if (contador_f_pintura != 0):
    promedio = acum_edad_f_pintura / contador_f_pintura
    print(f"Promedio de edad de los encuestados de género Femenino que votaron PINTURA: {promedio} años")
else:
    print("No se ingresaron mujeres")


mas_encuestado = "OTRO"
if (contador_f > contador_m and contador_f > contador_o):
    mas_encuestado = "FEMENINO"
elif (contador_m > contador_o):
    mas_encuestado = "MASCULINO"
print(f"El genero con mas encuestados fue: {mas_encuestado}")