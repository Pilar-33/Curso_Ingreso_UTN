from os import system
system("cls")
#CONDICIONAL SIMPLE
#Ejercicio 1: Verificación de número par o impar.
#Solicitar un número al usuario e informar si el mismo es par o impar

print("  PROGRAMA DE VERIFICACIÓN DE NÚMERO PAR O IMPAR" + "\n" + "*"*50)
#print("*"*50)
number = int(input("Ingrese un número: "))

if number % 2 == 0:
    msje = f"El número {number} es par"
else:
    msje = f"El número {number} es impar"
print("*"*50 + f"\n{msje}")
