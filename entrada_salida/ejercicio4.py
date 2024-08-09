from os import system
system('cls')

'''Ejercicio4: Tenemos que obtener los valores (por input) que el usuario 
nos ingrese (operador_a y operador_b), transformarlosennúmerosenteros, 
realizar la operación suma y luego mostrar el resultado de la misma utilizando print.'''

operador_a = int(input("Ingrese el primer número: "))
operador_b = int(input("Ingrese el segundo número: "))

suma = operador_a + operador_b

print(f"El resultado de la suma es: {suma}")