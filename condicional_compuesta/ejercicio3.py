from os import system
system('cls')
#CONDICIONAL COMPUESTO
#Ejercicio3: Verificación de pertenencia a grupo según edad y género. 
#Solicitar edad y género (femenino/masculino) al usuario, dependiendo de los datos ingresados 
# informarle el Grupo al que pertenece: 
# Femeninos mayores de edad => “Grupo A” 
# Masculinos mayores de edad => “Grupo B”
# NOTA: En el caso que no corresponda a ningún grupo, informar.


print("   VERIFICACIÓN DE PERTENENCIA A GRUPO SEGÚN EDAD Y GENERO" + "\n" + "*"*60)

edad = int(input("Ingrese la edad: "))

if (edad > 0):
    genero = input("Ingrese genero(femenino/masculino): ")

    if edad > 17 and genero == "femenino":
        msje = "Grupo A"
    elif edad > 17 and genero == "masculino":
        msje = "Grupo B"
    else:
        msje = "No pertenece a ningún grupo"
else:
    msje = "Edad no valida"
    
print("*"*60 + "\n" + msje)


