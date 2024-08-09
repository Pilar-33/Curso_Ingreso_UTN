from os import system
system('cls')
'''Una empresa internacional está realizando un estudio de mercado para decidir cuál 
será la nueva plataforma de entretenimiento que se lanzará en el mercado argentino y en la cual invertirán.
Las posibles franquicias son las siguientes: Hulu, Vix+ o CODA.
Para ello, se realizará una encuesta mediante un sistema de voto electrónico, 
con el propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
Se ingresa de cada encuestado:
Nombre
Edad (no menor a 18)
Tiene suscripción a algún servicio de streaming (sí-no)
Género (Masculino - Femenino - No binario - Otro)
Voto (Hulu, Vix+, CODA)
Se solicita realizar las siguientes búsquedas:

1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49  que votaron por Hulu.
2. Nombre, género y edad del encuestado de menor edad que votó por Hulu.
3. Hallar el porcentaje de encuestados mayores de 25 años que tienen suscripción CODA.
4. Determinar el promedio de edad de los encuestados que votaron por Vix+.
5. Contar cuántos encuestados votaron por cada franquicia y determinar cuál tuvo más votos.'''

votos_carga = "si"
cantidad_hulu_m = 0
cantidad_c_25 = 0
flag_menor_h =  True
cantidad_votos = 0
suma_edad_v = 0
cantidad_v = 0
cantidad_h = 0
cantidad_c = 0
while votos_carga == "si":
    nombre = input("Nombre: ")
    
    edad = int(input("Edad: "))
    while edad < 18:
        edad = int(input("Edad no válida!!!. \nIngrese edad (no menor a 18): "))
    genero = input("Género (M/F/NB/O): ")
    while genero != "M" and genero != "F" and genero != "NB" and genero != "O":
        genero = input("Género no válido!!!. \nIngrese género (M/F/NB/O): ")
    
    voto = input("Voto (H/V/C): ")
    while voto != "H" and voto != "V" and voto != "C":
        voto = input("Voto no válido!!!. \nIngrese voto(H/V/C): ")
    
    if voto == "H":
        cantidad_h +=1
        if genero =="M" and (edad > 17 and edad < 26) or (edad > 35 and edad < 50):
            cantidad_hulu_m += 1
        
        if flag_menor_h == True:
            flag_menor_h = False
            menor_h = edad
            nombre_menor_h = nombre
            genero_menor_h = genero
        elif edad < menor_h:
            menor_h = edad
            nombre_menor_h = nombre
            genero_menor_h = genero
    elif voto == "C":
        cantidad_c +=1
        if edad > 25:
            cantidad_c_25 += 1
    elif voto == "V":
        suma_edad_v += edad
        cantidad_v += 1
    
    cantidad_votos =+1
    votos_carga = input("Desea ingresar voto (si/no): ")

#porcentaje mayores 25 CODA
porcentaje_coda = (cantidad_c_25* 100) / cantidad_votos 

#promedio v
promedio_v = suma_edad_v / cantidad_v 


#mas votado
mas_votado = "V"
if cantidad_c > cantidad_h and cantidad_c > cantidad_v:
    mas_votado = "C"
elif cantidad_h > cantidad_c and cantidad_h > cantidad_v:
    mas_votado = "H"

msje = f"                                      RESUMEN BUSQUEDAS\n"
msje += f"===============================================================================================\n"
msje += f"1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49  que votaron por Hulu: {cantidad_hulu_m}\n"
msje += f"2. Nombre, género y edad del encuestado de menor edad que votó por Hulu: {nombre_menor_h}||{genero_menor_h}||{menor_h} años\n"
msje += f"3. Hallar el porcentaje de encuestados mayores de 25 años que tienen suscripción CODA: {porcentaje_coda}\n"
msje += f"4. Determinar el promedio de edad de los encuestados que votaron por Vix+: {promedio_v}\n"
msje += f"5. Contar cuántos encuestados votaron por cada franquicia y determinar cuál tuvo más votos: Hulu: {cantidad_h}\n Vix+:{ cantidad_v}\n CODA: {cantidad_c}\nFranquicia mas vodada: {mas_votado}"
print(msje)