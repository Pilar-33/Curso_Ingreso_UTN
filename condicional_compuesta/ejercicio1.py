from os import system
system('cls')
#CONDICIONAL COMPUESTO
#Ejercicio1: Verificación de número dentro de un rango. 
# Solicitar un número entero al usuario entre el 1 y el 100 y
# validar si se encuentra dentro del rango solicitado. 
# Informar si se encuentra dentro o fuera del rango.


print("      PROGRAMA QUE VERIFICA NÚMERO DENTRO DE UN RANGO" + "\n" + "="*60)
number = int(input("Ingrese un número entero entre el 1 y el 100: "))

if number > 0 and number < 101:
    msje = f"El {number} está dentro de rango"
else:
    msje = f"El {number} está fuera de rango"

print("="*60 + "\n" + msje)
