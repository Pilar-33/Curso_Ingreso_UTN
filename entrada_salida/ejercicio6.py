from os import system
system("cls")
'''Ejercicio6: Tenemos que obtener los valores (por input) que el 
usuario nos ingrese (operador_a y operador_b), transformar los en números enteros, 
realizar la operación que nos permita obtener el resto de una división y luego mostrar 
el resultado de la misma utilizando print. '''

operador_a = int(input("Ingrese primer número entero: "))
operador_b = int(input("Ingrese segundo número entero: "))

resto = operador_a % operador_b

print(f"El resto de dividir {operador_a} por {operador_b} es: {resto}")