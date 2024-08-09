#Enunciado 1 : De 5 personas que ingresan al hospital se deben tomar y validar los siguientes datos.
# ● nombre 
# ● temperatura, entre 35 y 42 
# ● sexo( f, m , nb ) 
# ● edad(mayor a 0) 
# pedir datos por prompt y mostrar por print 
# Punto A-informar cual fue el sexo mas ingresado 
# Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre.
# Punto C - por el número de DNI del alumno DNI terminados en 0 o 1
# 1)informar la cantidad de personas de sexo femenino 
# 2) la edad promedio de personas de sexo masculino 
# 3) el nombre de la persona la persona de sexo nb con más temperatura(si la hay)
# DNI terminados en 2 o 3
# 1) informar la cantidad de personas de sexo masculino 
# 2) la edad promedio de personas de sexo nb 
# 3) el nombre de la persona de sexo femenino con la temperatura mas baja(si la hay)
# DNI terminados en 4 o 5
# 1)informar la cantidad de personas de sexo nb 
# 2) la edad promedio de personas de sexo femenino 
# 3) el nombre de la persona la persona de sexo masculino con la temperatura mas baja(si la hay)
# DNI terminados en 6 o 7
# 1)informar la cantidad de personas mayores de edad (desde los 18 años) 
# 2)la edad promedio en total de todas las personas mayores de edad (18 años) 
# 3) el nombre de la persona la persona de sexo masculino con la temperatura mas baja(si la hay)
# DNI terminados en 8 o 9
# 1)informar la cantidad de personas menores de edad (menos de 18 años) 
# 2)la temperatura promedio en total de todas las personas menores de edad 
# 3) el nombre de la persona de sexo femenino con la temperatura mas baja(si la hay)



contador = personas_con_fiebre = personas_sin_fiebre = numero_f = numero_m = numero_nb = 0
dni_0_1_f=dni_0_1_m_edad_total=dni_0_1_m_count=dni_0_1_nb_max_temp=0
dni_0_1_nb_max_temp_nombre = " "
dni_2_3=dni_2_3_m_edad_total=0
dni_4_5=dni_6_7=dni_8_9=0
print("="*35)
print("     INGRESE DATOS DEL PACIENTE")
print("="*35)
while contador < 5:
    #Ingreso del nombre de los pacientes
    nombre = input(f"Nombre del {contador+1}° paciente: ")
    
    #Ingreso de temperatura y validación
    temperatura = float(input(f"Temperatura del {contador+1}° paciente (35 y 42):  "))
    while not(35<=temperatura<=42):
        temperatura = float(input(f"Vuelva ingresar la Temperatura del {contador+1}° paciente: "))
    
    if 37 <= temperatura <= 42:
        personas_con_fiebre += 1
        
    else:
        personas_sin_fiebre +=1
    
    #Ingreso de sexo y validación
    sexo = input(f"Sexo del {contador+1}° paciente (f, m, nb):  ").lower()
    while sexo not in ("f", "m", "nb"):
        sexo = input(f"Vuelva ingresar el sexo del {contador+1}° paciente: ").lower()

    if sexo == "f":
        numero_f += 1
    elif sexo == "m":
        numero_m += 1
    else:
        numero_nb += 1

    # Ingreso de edad y validación
    edad = int(input(f"Edad del {contador+1}° paciente (mayor a 0):  "))
    while edad <= 0:
        edad = int(input(f"Vuelva ingresar la Edad del {contador+1}° paciente: "))

    # Analizando el DNI y validando según punto C
    dni = int(input(f"DNI del {contador+1}° paciente:  "))
    # Verificar si el DNI es correcto o volver a ingresar
    while dni not in range(10000000, 100000000):
        dni = int(input(f"Vuelva ingresar el DNI del {contador+1}° paciente: "))
    
    # Por el número de DNI del alumno DNI terminados en 0 o 1
    if dni % 10 in [0, 1]:
        if sexo == "f":
            dni_0_1_f += 1
        elif sexo == "m":
            dni_0_1_m_edad_total += edad
            dni_0_1_m_count += 1
        elif sexo == "nb":
            if temperatura > dni_0_1_nb_max_temp:
                dni_0_1_nb_max_temp = temperatura
                dni_0_1_nb_max_temp_nombre = nombre

    # Por el número de DNI del alumno DNI terminados en 2 o 3
    elif dni % 10 in [2, 3]:
        if sexo == "m":
            dni_2_3 += 1
        elif sexo == "nb":
            if temperatura > dni_0_1_nb_max_temp:
                dni_0_1_nb_max_temp = temperatura
                dni_0_1_nb_max_temp_nombre = nombre
    contador +=1
    print("")

print("="*70)
#Analizando el sexo mas ingresado
print("Punto A:")
max_count = numero_f
max_sexo = "femenino(f)"

if numero_m > max_count:
    max_count = numero_m
    max_sexo = "masculino(m)"
elif numero_m == max_count:
    max_sexo += " y masculino(m)"

if numero_nb > max_count:
    max_count = numero_nb
    max_sexo = "no binario(nb)"
elif numero_nb == max_count:
    max_sexo += " y no binario(nb)"

if "y" in max_sexo:
    print(f"        ● Hubo un empate entre los siguientes sexos: {max_sexo}: {max_count}")
    
else:
    print(f"        ● Sexo más ingresado fue {max_sexo}: {max_count}")
    
print(f"""Punto B:
        ● Porcentaje de personas con fiebre es: {(personas_con_fiebre*100)/contador}%
        ● Porcentaje de personas sin fiebre es: {(personas_sin_fiebre*100)/contador}%""")

print("Punto C:")
print("\na) Resultados para DNI terminados en 0 o 1:")
print(f"1) Cantidad de personas de sexo femenino: {dni_0_1_f}")
if dni_0_1_m_count > 0:
    print(f"2) Edad promedio de personas de sexo masculino: {dni_0_1_m_edad_total / dni_0_1_m_count:.2f}")
else:
    print("2) No hay personas de sexo masculino en este grupo")
if dni_0_1_nb_max_temp_nombre:
    print(f"3) Persona de sexo nb con más temperatura: {dni_0_1_nb_max_temp_nombre} ({dni_0_1_nb_max_temp}°C)")
else:
    print("3) No hay personas de sexo nb en este grupo")

print("\nb) Resultados para DNI terminados en 2 o 3:")