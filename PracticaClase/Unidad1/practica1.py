#1) Escribe un programa muestre por consola “Hola UTN”.
print("Hola UTN")

# 2) Escribe un programa que muestre por consola el resultado de sumar 3 + 5.
print(3 + 5)

# 3) Escribe un programa que muestre por consola el resultado de restar 10-5
print(10-5)

#4) Escribe un programa que muestre por consola el resultado de restar 10-15
print(10-15)

# 5) Escribe un programa que muestre por consola el resultado de multiplicar 4*10
print(4*10)

# 6) Escribe un programa que muestre por consola el resultado de dividir 10/2
print(10/2)

#7) Escribe un programa que muestre por consola el resultado de dividir 10/0.detalla en comentarios qué es lo que sucede al dividir por 0.
try:
    print(10/0) # Error: ZeroDivisionError: division by zero
except Exception as e:
    print(f"No se puede dividir por 0: {e}")

# 8) Escribe un programa que muestre por consola el resultado de la siguiente
 #operación (10+3) * (6+6), ¿qué sucede si realizas la misma operación pero sin los paréntesis?
print((10+3)*(6+6))
print(10+3*6+6)

# 9) Escribe un programa que muestre por consola el resultado de la siguiente operación 10%2
print(10%2)

# 10) Escribe un programa que muestre por consola la siguiente operación 10%3
print(10%3)

#11) Crear un programa (suma, resta, multiplicación, y división),
#se deberá generar dos variables del tipo “variableA” y “variableB”,
#asignarles un valor del tipo número a cada una de ellas.
#El programa deberá mostrar por consola el resultado de realizar las 4
#operaciones aritméticas mencionadas entre ellas.

varibleA = 8
varibleB = 10

suma = varibleA + varibleB
resta = varibleA - varibleB
multiplicacion = varibleA * varibleB
division = varibleA / varibleB

print(f"Suma de: {varibleA} + {varibleB} = {suma}")
print(f"Resta de: clear{varibleA} - {varibleB} = {resta}")
print(f"Multiplicacion de: {varibleA} * {varibleB} = {multiplicacion}")
print(f"Division de: {varibleA} / {varibleB} = {division}")