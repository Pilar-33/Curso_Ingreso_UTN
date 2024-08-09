from os import system
system('cls')

'''Ejercicio5: Se deberá crear un programa que muestre cada operación (suma, resta, multiplicación, y división), 
tenemos que obtener los valores (porinput) que el usuario nos ingrese (operador_a y operador_b), 
transformarlosennúmerosenteros, realizar dicha operación y 
luego mostrar el resultado de la misma utilizando print.'''

operador_a = int(input("Ingrese el primer número: "))
operador_b = int(input("Ingrese el segundo número: "))

# operaciones
suma = operador_a + operador_b
resta = operador_a - operador_b
multiplicacion = operador_a * operador_b
div = operador_a / operador_b
msje = f''' 
                    OPERACIONES
    =========================================
    Suma: {operador_a} + {operador_b} = {suma}
    Resta: {operador_a} - {operador_b} = {resta}
    Multiplicación: {operador_a} * {operador_b} = {multiplicacion}
    Division: {operador_a} / {operador_b} = {div:.2f}'''
    
print(msje)