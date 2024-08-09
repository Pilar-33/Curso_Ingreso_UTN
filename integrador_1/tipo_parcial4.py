from os import system
system('cls')
'''
Un jugador de League of Legends tiene un fin de semana libre y 
va a jugar partidas hasta que se canse.

Para mejorar su jugabilidad, por cada partida jugada va a registrar:
    * Modo de juego ("Normal", "Clasificatoria", "ARAM")
    * Nombre del personaje que usó
    * La cantidad de asesinatos a favor (No puede ser negativo)
    * Muertes en contra (No puede ser negativo)
    * Asistencias a favor. (No puede ser negativo, hasta 40)

Consignas:
    0) - El modo de juego más jugado.
    1) - El modo de juego menos jugado.
    2) - El personaje con el cual murió más.
    3) - El personaje con el cual asistio más.
    4) - El promedio de asesinatos a favor en modo Clasificatoria.
    5) - El promedio de muertes en contra en modo ARAM.
    6) - El promedio de asistencias en modo Normal.
    7) - De la partida con mas muertes en contra, el nombre del personaje y el modo de juego.
    8) - De la partida con mas asistencias a favor, el nombre del personaje y el modo de juego.
    9) - De la partida con mas asesinatos a favor, el nombre del personaje y el modo de juego.'''

otra_partida = "si"
contador_normal = 0
contador_clasificatoria = 0
contador_aram = 0
flag_murio_mas = True
flag_asistio_mas = True
flag_mas_muertes =True
flag_mas_asistencias =True
flag_mas_asesinatos = True
suma_asesinatos_C = 0
suma_muertes_A = 0
suma_asistencias_N = 0

while otra_partida == "si":
    modo_juego = input("Modo de juego (Normal/Clasificatoria/ARAM): ")
    while modo_juego != "Normal" and modo_juego != "Clasificatoria" and modo_juego != "ARAM":
        modo_juego = input("Modo de juego (Normal/Clasificatoria/ARAM): ")
    
    nombre_personaje = input("Nombre del personaje que uso: ")
    
    cantidad_asesinatos = int(input("Cantidad de asesinatos a favor: "))
    while cantidad_asesinatos < 0:
        cantidad_asesinatos = int(input("Cantidad de asesinatos a favor (No puede ser negativo): "))
    
    muerte_contra = int(input("Muertes en contra: "))
    while muerte_contra < 0:
        muerte_contra = int(input("Muertes en contra (No puede ser negativo): "))
    
    asistencia_favor = int(input("Asistencias a favor: "))
    while asistencia_favor < 0  or asistencia_favor > 40:
        asistencia_favor = int(input("Asistencias a favor (No puede ser negativo): "))
    
    if modo_juego == "Normal":
        contador_normal += 1
        suma_asistencias_N += asistencia_favor
    elif modo_juego == "Clasificatoria":
        contador_clasificatoria +=1
        suma_asesinatos_C += cantidad_asesinatos
    else:
        contador_aram += 1
        suma_muertes_A += muerte_contra
        
    if flag_murio_mas == True:
        flag_murio_mas =False
        muerte_maxima = muerte_contra
        nombre_personaje_maximo = nombre_personaje
    elif muerte_contra > muerte_maxima:
        muerte_maxima = muerte_contra
        nombre_personaje_maximo = nombre_personaje
    
    if flag_asistio_mas == True:
        flag_murio_mas = False
        asistencia_maxima = asistencia_favor
        nombre_personaje_maximo_asistencia = nombre_personaje
    elif asistencia_favor > asistencia_maxima:
        asistencia_maxima = asistencia_favor
        nombre_personaje_maximo_asistencia = nombre_personaje
    
    if flag_mas_muertes ==True:
        flag_mas_muertes = False
        mas_muertes = muerte_contra
        nombre_mas_muertes = nombre_personaje
        juego_mas_muertes = modo_juego
    elif muerte_contra > mas_muertes:
        mas_muertes = muerte_contra
        nombre_mas_muertes = nombre_personaje
        juego_mas_muertes = modo_juego
    
    if flag_mas_asistencias == True:
        flag_mas_asistencias = False
        mas_asistencias = asistencia_favor
        nombre_mas_asistencias = nombre_personaje
        juego_mas_asistencias = modo_juego
    elif asistencia_favor > mas_asistencias:
        mas_asistencias = asistencia_favor
        nombre_mas_asistencias = nombre_personaje
        juego_mas_asistencias = modo_juego
    
    if flag_mas_asesinatos == True:
        flag_mas_asesinatos = False
        mas_asesinatos = cantidad_asesinatos
        nombre_mas_asesinatos = nombre_personaje
        juego_mas_asesinatos = modo_juego
    elif cantidad_asesinatos > mas_asesinatos:
        mas_asesinatos = cantidad_asesinatos
        nombre_mas_asesinatos = nombre_personaje
        juego_mas_asesinatos = modo_juego

    otra_partida = input("Otra partida (si/no): ")
    
#0) - El modo de juego más jugado.
if contador_normal == contador_aram and contador_normal == contador_clasificatoria:
    juego_mas_jugado = "Igual cantidad de juegos: Normal, Clasificatoria y Normal" 
elif contador_normal > contador_clasificatoria and contador_normal > contador_aram:
    juego_mas_jugado = "Normal"
elif contador_clasificatoria > contador_normal and contador_clasificatoria > contador_aram:
    juego_mas_jugado = "Clasificatoria"
else:
    juego_mas_jugado = "ARAM"

#1) - El modo de juego menos jugado.
if contador_normal == contador_aram and contador_normal == contador_clasificatoria:
    juego_menos_jugado = "No hay"
elif contador_normal == contador_aram:
    juego_menos_jugado = "Normal y ARAM"
elif contador_normal == contador_clasificatoria:
    juego_menos_jugado = "Normal y Clasificatoria"
elif contador_clasificatoria == contador_aram:
    juego_menos_jugado = "Clasificatoria y ARAM"
elif contador_normal < contador_clasificatoria and contador_normal < contador_aram:
    juego_menos_jugado = "Normal"
elif contador_clasificatoria < contador_normal and contador_clasificatoria < contador_aram:
    juego_menos_jugado = "Clasificatoria"
else:
    juego_menos_jugado = "ARAM"

promedio_asesinato_c = suma_asesinatos_C/contador_clasificatoria
promedio_muertes_a = suma_muertes_A/contador_aram
promedio_asistencia_n = suma_asistencias_N/contador_normal

msje = f"                                   RESUMEN DE PARTIDAS\n"
msje += f"===============================================================================================\n"
msje += f"0) Modo de juego más jugado es: {juego_mas_jugado}\n"
msje += f"1) Modo de juego menos jugado es: {juego_menos_jugado}\n"
msje += f"2) Personaje con el cual murió más: {nombre_personaje_maximo}\n"
msje += f"3) Personaje con el cual asistio más: {nombre_personaje_maximo_asistencia}\n"
msje += f"4) Promedio de asesinatos a favor en modo Clasificatoria: {promedio_asesinato_c}%\n"
msje += f"5) Promedio de muertes en contra en modo ARAM: {promedio_muertes_a}%\n"
msje += f"&) Promedio de asistencias en modo Normal: {promedio_asistencia_n}%\n"
msje += f"7) Partida con mas muertes en contra, el nombre del personaje y el modo de juego: {nombre_mas_muertes}||{juego_mas_muertes}\n"
msje += f"8) Partida con mas asistencias a favor, el nombre del personaje y el modo de juego: {nombre_mas_asistencias}||{juego_mas_asistencias}\n"
msje += f"9) Partida con mas asesinatos a favor, el nombre del personaje y el modo de juego: {nombre_mas_asesinatos}||{juego_mas_asesinatos}"

print(msje)