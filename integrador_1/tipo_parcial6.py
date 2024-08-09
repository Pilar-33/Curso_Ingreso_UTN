from os import system
system('cls')
'''
Se nos ha solicitado desarrollar una aplicación para llevar registro de las 
entradas vendidas en el Estadio River Plate, para el concierto de Taylor Swift. 
Para ello, se solicitará al usuario la siguiente información al momento de 
comprar cada entrada:
    * Nombre del comprador
    * Edad (no menor a 16)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Platea)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)
Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.
 * Lista de precios: 
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000
Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 
Consignas:
    #! 0) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #! 1) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.
    #! 2) - Calcula el número total de entradas compradas por personas mayores de 30 años y 
    #!          su precio promedio.
    #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjeta de débito  respecto al total de personas en la lista.
    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa (OMITO).
    #! 5) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
    #!          los aplicados a tarjetas de crédito (OMITO)
    #! 6) - Encuentra los nombres y las edades de la personas que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (OMITO)
    #! 7) - Encuentra la cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.
    #! 8) - Calcula el monto total recaudado por la venta de entradas de tipo "General" y 
    #!          pagadas con tarjeta de crédito por personas cuyas edades son múltiplos de 5.
    #! 9) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
'''
general = 16000
campo = 25000
platea = 30000
dcto_c = 0.20
dcto_d = 0.15
total_descuentos = 0
total_descuentos_c = 0
cantidad_general = 0
cantidad_platea = 0
cantidad_platea_d = 0
total_entradas_30 = 0
suma_precio_30 = 0
masculino_campo = 0
femenino_campo = 0
otro_campo = 0
cantidad_g_c = 0
suma_edad_g_c = 0
cantidad_g_d = 0
flag_precio_alto = 0
monto_general_c = 0
monto_platea_d = 0
cantidad_platea_primo = 0
es_primo = True

carga_entrada = "si"

while carga_entrada == "si":
    nombre = input("Nombre: ")

    edad = int(input("Edad: "))
    while edad < 16:
        edad = int(input("Edad (debe ser mayor o igual a 16): "))

    genero = input("Género (m,f,o): ")
    while genero != "m" and genero != "f" and genero != "o":
        genero = input("Error. Género (m,f,o): ")

    tipo_entrada = input("Tipo de entrada (general, campo, platea): ")
    while tipo_entrada != "general" and tipo_entrada != "campo" and tipo_entrada != "platea":
        tipo_entrada = input("Error. Tipo de entrada (general, campo, platea): ")

    medio_pago = input("Medio de pago (credito, efectivo, debito): ")
    while medio_pago!= "credito" and medio_pago!= "efectivo" and medio_pago!= "debito":
        medio_pago = input("Error. Medio de pago (credito, efectivo, debito): ")

    precio_entrada = float(input("Precio de la entrada: "))

    if tipo_entrada == "campo":
        if genero == "m":
            masculino_campo += 1
        elif genero == "f":
            femenino_campo += 1
        elif genero == "o":
            otro_campo += 1  
    elif tipo_entrada == "general":
        cantidad_general += 1
        if medio_pago == "credito":
            cantidad_g_c += 1
            suma_edad_g_c += edad
            if edad % 5 == 0:
                descuento_c = precio_entrada * 0.20
                precio_pagar_c  = precio_entrada - descuento_c
                #monto_general = precio_entrada * (1 - 0.20)
                monto_general_c += precio_pagar_c
        elif medio_pago == "debito":
            cantidad_g_d += 1
            if flag_precio_alto == True:
                flag_precio_alto = False
                precio_alto = precio_entrada
                nombre_precio_alto = nombre
                edad_precio_alto = edad
            elif precio_entrada > precio_alto:
                precio_alto = precio_entrada
                nombre_precio_alto = nombre
                edad_precio_alto = edad      
    elif tipo_entrada == "platea":
        cantidad_platea += 1
        if edad > 1:
            divisor = 2
            while divisor < edad and es_primo == True:
                if edad % divisor == 0:
                    es_primo = False
                divisor += 1

            if es_primo == True:
                cantidad_platea_primo += 1
            es_primo = True

        if medio_pago == "debito":
            cantidad_platea_d += 1
            if edad % 6 == 0:
                descuento_d = precio_entrada * 0.15
                precio_pagar_d  = precio_entrada - descuento_d
                #monto_platea = precio_entrada * (1 - 0.20)
                monto_platea_d += precio_pagar_d
    
    if edad > 30:
        total_entradas_30 += 1
        if medio_pago == "credito":
            precio_entrada = general * (1 - dcto_c)
        elif medio_pago == "debito":
            precio_entrada = general * (1 - dcto_d)
        else:
            precio_entrada = general

        suma_precio_30 += precio_entrada

    if medio_pago == "credito":
        precio_entrada = general * (1 - dcto_c)
        total_descuentos += general * dcto_c
        total_descuentos_c += general * dcto_c
    elif medio_pago == "debito":
        precio_entrada = general * (1 - dcto_d)
        total_descuentos += general * dcto_d
    else:
        precio_entrada = general


    cantidad_general += 1
    carga_entrada = input("Otra entrada (si/no): ")

genero_mas_frecuente = "Otro"
if masculino_campo > femenino_campo and masculino_campo > otro_campo:
    genero_mas_frecuente = "Masculino"
elif femenino_campo > masculino_campo and femenino_campo > otro_campo:
    genero_mas_frecuente = "Femenino"


if cantidad_g_c != 0:
    promedio_g_c = suma_edad_g_c/cantidad_g_c
else:
    promedio_g_c = 0

if total_entradas_30 != 0:
    precio_promedio_30 = suma_precio_30/total_entradas_30
else:
    precio_promedio_30 = 0

porcentaje_platea_d = (cantidad_platea_d * 100) / cantidad_general

msje = f"0) Determina el género más frecuente entre las personas que compraron entradas de tipo 'Campo': {genero_mas_frecuente}\n"
msje += f"1) Determina cuántas personas compraron entradas de tipo 'General' pagando con tarjeta de crédito y su edad promedio: {cantidad_g_c} persona(s)||{suma_edad_g_c}\n"
msje += f"2) Calcula el número total de entradas compradas por personas mayores de 30 años y su precio promedio: {precio_promedio_30}\n"
msje += f"3) Calcula el porcentaje de personas que compraron entradas de tipo 'Platea' y pagaron con tarjeta de débito respecto al total de personas en la lista: {porcentaje_platea_d}%\n"
msje += f" 4) Cuál es el total de descuentos en pesos que aplicó la empresa (OMITO): {total_descuentos} pesos\n"
msje += f"5) Determina el total de descuentos en pesos que aplicó la empresa, pero solo de los aplicados a tarjetas de crédito (OMITO): {total_descuentos_c} pesos\n"
msje += f" 6) Encuentra los nombres y las edades de la personas que pagó el precio más alto por una entrada de tipo 'General' y pagó con tarjeta de débito (OMITO): {nombre_precio_alto}||{edad_precio_alto}\n"
msje += f"7) - Encuentra la cantidad de personas que compraron entradas de tipo 'Platea' y cuya edad es un número primo: {cantidad_platea_primo}\n"
msje += f"8) Calcula el monto total recaudado por la venta de entradas de tipo 'General' pagadas con tarjeta de crédito por personas cuyas edades son múltiplos de 5: ${monto_general_c}\n"
msje += f"9) Calcula el monto total recaudado por la venta de entradas de tipo 'Platea' y pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6: ${monto_platea_d}"
print(msje)

