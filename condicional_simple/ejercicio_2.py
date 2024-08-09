from os import system
system('cls')
#CONDICIONAL SIMPLE
#Ejercicio 2: Comparación de dos números enteros
#Solicitar un número al usuario e informar si uno es mayor 
# que el otro o si son iguales.

print("  PROGRAMA QUE ANALIZA QUE NÚMERO ES MAYOR/MENOR O IGUALES" + "\n" + "*"*60)
number1 = int(input("Ingrese un número entero: "))
number2 = int(input("Ingrese otro número entero: "))


if number1 > number2:
    msje = f"El número {number1} es mayor que {number2}"
elif number1 < number2:
    msje = f"El número {number2} es mayor que {number1}"
else:
    msje = f"Los números {number1} y {number2} son iguales"

print("*"*60 + "\n" + f"{msje}")