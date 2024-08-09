from os import system
system('cls')
#CONDICIONAL COMPUESTO
# Ejercicio4: Determinar el mayor de 3 números
#Solicitar tres números distintos al usuario y mostrar el mayor.

print("       PROGRAMA QUE DETERMINA EL MAYOR DE 3  NÚMEROS" + "\n" + "*"*60)

number1 = float(input("Ingrese primer número: "))
number2 = float(input("Ingrese segundo número: "))
number3 = float(input("Ingrese el tercer número: "))

if number1 > number2 and number1 > number3:
    msje = f"El número mayor es {number1}"
elif number2 > number1 and number2 > number3:
    msje = f"El número mayor es {number2}"
elif number1 == number2 and number1 == number3:
    msje = "Los números son iguales, no existe número mayor"
else:
    msje = f"El número mayor es {number3}"

print("*"*60 + "\n" + msje)