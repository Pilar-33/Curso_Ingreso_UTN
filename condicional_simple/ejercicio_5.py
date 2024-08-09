from os import system
system('cls')
#CONDICIONAL SIMPLE
#Ejercicio5:Determinar si un año es bisiesto o no Considerando el siguiente 
# diagrama de flujo para calcular si un año es bisiesto o no.

print(" PROGRAMA QUE DETERMINA SI UN AÑO ES BISIESTO O NO" + "\n" + "*"*50)
anio = int(input("Ingrese un año: "))

if anio < 0:
    msje = "El año no puede ser negativo"
elif anio == 0:
    msje = "El año no puede ser 0"
elif (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
    msje = f"El año {anio} es bisiesto"
else:
    msje = f"El año {anio} no es bisiesto"

print("*"*50 + "\n" +msje)