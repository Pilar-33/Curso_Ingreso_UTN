from os import system
system('cls')
'''Nos encargan el desarrollo de una aplicación que le permita a sus usuarios inscribirse a 
un listado de viajeros para un nuevo transbordador de SpaceX:

#?Para ello deberás programar el botón 'Cargar Viajeros' para poder cargar los siguientes datos de 5 personas:
#?  * Nombre
#?  * Altura (entre 60 cm y 200 cm)
#?  * Peso (entre 40 kilos y 250 kilos)
#?  * Edad (entre 1 y 100 ) 

B) Al presionar el botón "Mostrar Datos Crudo" se deberán listar todos los datos de los usuarios y 
    su posición en la lista (por terminal) 

    6) 
        #!A- El nombre de las personas que NO superen la edad promedio
        #!B- La cantidad de personas de menos de 160 cm de altura
    7) 
        #!A- El nombre de las personas que NO superen la altura promedio
        #!B- La cantidad de personas de menos de 80 kilos
    8)
        #!A- El nombre de las personas que NO superen el peso promedio
        #!B- La cantidad de personas de más  de 50 kilos
    9) 
        A- El nombre de las personas que SI superen el peso promedio
        #!B- La cantidad de personas de menos de 18 años
'''
################################################################################
flag_menor_peso = True
flag_mayor_peso = True
flag_mayor_altura = True
flag_menor_altura = True
flag_mayor_edad = True
flag_menor_edad = True
carga_datos = 0
cantidad_usuarios = 0
suma_edades = 0
suma_altura = 0
suma_peso = 0
cantidad_mayores_50 = 0
cantidad_menores_50 = 0
cantidad_menores_18 = 0
cantidad_kilos_50 = 0
cantidad_kilos_80 = 0
cantidad_kilos_100 = 0
cantidad_kilos_80_menos = 0
cantidad_altura_100 = 0
cantidad_altura_170 = 0
cantidad_altura_160 = 0

#Listas
nombres = []
edades = []
alturas = []
pesos = []
msje = ""
#Cargar datos
print("          TRANSBORDADOR DE SPACEX" + "\n" + "*"*50)
while carga_datos < 5:
    nombre = input("Nombre: ")
    
    altura = float(input("Altura (entre 60 cm y 200 cm): "))
    while altura < 60 or altura > 200:
        altura = float(input("Inválida, Ingrese altura (entre 60 cm y 200 cm): "))

    peso = float(input("Peso (entre 40 kilos y 250 kilos): "))
    while peso < 40 or peso > 250:
        peso = float(input("Inválida, Ingrese peso (entre 40 kilos y 250): "))
    
    edad = int(input("Edad (entre 1 y 100 ): "))
    while edad < 1 or edad > 100:
        edad = int(input("Inválida, Ingrese edad (entre 1 y 100): "))
    
    #Almacenar datos
    nombres.append(nombre)
    edades.append(edad)
    alturas.append(altura)
    pesos.append(peso)
    
    #B) Mostrar datos
    msje += \
    f'''
    DATOS DEL USUARIO Nro {carga_datos+1}
    Nombre: {nombre} 
    Altura: {altura} cm
    Peso: {peso} kilos
    Edad: {edad} años\n'''
    
    if flag_menor_peso == True:
        flag_menor_peso = False
        menor_peso = peso
        nombre_menor_peso = nombre
    elif peso < menor_peso:
        menor_peso = peso
        nombre_menor_peso = nombre
        
    if flag_mayor_peso == True:
        flag_mayor_peso = False
        mayor_peso = peso
        nombre_mayor_peso = nombre
    elif peso > mayor_peso:
        mayor_peso = peso
        nombre_mayor_peso = nombre
        
    
    if edad > 50:
        cantidad_mayores_50 += 1
    if edad < 50:
        cantidad_menores_50 += 1
    if edad < 18:
        cantidad_menores_18 += 1
        
    if peso > 80:
        cantidad_kilos_80 += 1
    if peso < 100:
        cantidad_kilos_100 += 1
    if peso < 80:
        cantidad_kilos_80_menos += 1
    if peso > 50:
        cantidad_kilos_50 += 1
    
    if flag_mayor_altura == True:
        flag_mayor_altura = False
        mayor_altura = altura
        nombre_mayor_altura = nombre
    elif altura > mayor_altura:
        mayor_altura = altura
        nombre_mayor_altura = nombre
    
    if flag_menor_altura == True:
        flag_menor_altura = False
        menor_altura = altura
        nombre_menor_altura = nombre
    elif altura < menor_altura:
        menor_altura = altura
        nombre_menor_altura = nombre
    
    if flag_mayor_edad == True:
        flag_mayor_edad = False
        mayor_edad = edad
        nombre_mayor_edad = nombre
    elif edad > mayor_edad:
        mayor_edad = edad
        nombre_mayor_edad = nombre
    
    if flag_menor_edad == True:
        flag_menor_edad = False
        menor_edad = edad
        nombre_menor_edad = nombre
    elif edad < menor_edad:
        menor_edad = edad
        nombre_menor_edad = nombre
    
    if altura > 100:
        cantidad_altura_100 += 1
    if altura < 170:
        cantidad_altura_170 += 1
    if altura < 160:
        cantidad_altura_160 += 1

    suma_edades += edad
    suma_altura +=  altura
    suma_peso += peso
    cantidad_usuarios += 1
    carga_datos +=1

#promedios
promedio_edad = suma_edades / cantidad_usuarios
promedio_altura = suma_altura / cantidad_usuarios
promedio_peso = suma_peso / cantidad_usuarios

#nombre que no supera promedio edad
nombres_no_superan_promedio_edad = []
for i in range(cantidad_usuarios):
    if edades[i] < promedio_edad:
        nombres_no_superan_promedio_edad.append(nombres[i])

#El nombre de las personas que NO superen la altura promedio
nombres_no_superan_promedio_altura = []
for i in range(cantidad_usuarios):
    if alturas[i] < promedio_altura:
        nombres_no_superan_promedio_altura.append(nombres[i])
        
#El nombre de las personas que NO superen el peso promedio
nombres_no_superan_promedio_peso = []
for i in range(cantidad_usuarios):
    if pesos[i] < promedio_peso:
        nombres_no_superan_promedio_peso.append(nombres[i])

#El nombre de las personas que SI superen la altura promedio
nombres_si_superan_promeedio_altura = []
for i in range(cantidad_usuarios):
    if alturas[i] >  promedio_altura:
        nombres_si_superan_promeedio_altura.append(nombres[i])


msjes = \
f'''
0)
    A- Nombre de la persona con el menor peso: {nombre_menor_peso}
    B- Cantidad de personas de más de 50 años: {cantidad_mayores_50}
1)
    A- Nombre de la persona con el mayor peso: {nombre_mayor_peso}
    B- Cantidad de personas de menos de 50 años: {cantidad_menores_50}
2)
    A- Nombre de la persona con la mayor altura: {nombre_mayor_altura}
    B- Cantidad de personas de más de 80 kilos: {cantidad_kilos_80}
3)
    A- Nombre de la persona con la menor altura: {nombre_menor_altura}
    B- Cantidad de personas de menos de 100: {cantidad_kilos_100}
4)
    A- Nombre de la persona con la mayor edad: {nombre_mayor_edad}
    B- Cantidad de personas de más de 100 cm de altura: {cantidad_altura_100}
5)
    A- Nombre de la persona con la menor edad: {nombre_menor_edad}
    B- cantidad de personas de menos de 170 cm de altura: {cantidad_altura_170}
6)
    A- Nombres de las personas que NO superan la edad promedio: {', '.join(nombres_no_superan_promedio_edad)}
    B- La cantidad de personas de menos de 160 cm de altura: {cantidad_altura_160}
7)
    A- El nombre de las personas que NO superen la altura promedio: {', '.join(nombres_no_superan_promedio_altura)}
    B- La cantidad de personas de menos de 80 kilos: {cantidad_kilos_80_menos}
8)
    A- El nombre de las personas que NO superen el peso promedio: {', '.join(nombres_no_superan_promedio_peso)}
    B- La cantidad de personas de más  de 50 kilos: {cantidad_kilos_50}
9)
    A- El nombre de las personas que SI superen el peso promedio: {', '.join(nombres_si_superan_promeedio_altura)}
    B- La cantidad de personas de menos de 18 años: {cantidad_menores_18}   '''
    
print(msje + "\n" + msjes)