from os import system
system('cls')
#3) Crear un programa que solicite al usuario que ingrese un número. 
# Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no coincidir con el rango, 
# volverlo a solicitar hasta que la condición se cumpla.



print("""
    +============================================+
        PROGRAMA QUE EVALUA EL NÚMERO INGRESADO
    +============================================+""")
number = int(input("Por favor, ingrese un número entre 0 y 9: "))

while number < 0 or number > 9:
    print("Número incorrecto. Está fuera del rango entre 0 y 9.")
    number = int(input("Ingrese nuevamente un número entre 0 y 9: "))
        
print(f'''
==============================================================
El número {number} es correcto, está dentro rango entre 0 y 9
Programa finalizado exitosamente!!!''')
