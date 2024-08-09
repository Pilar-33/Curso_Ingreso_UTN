from os import system
system('cls')
# 5) Crear unprogramaquealingresar un número puedecalcular si es mayor, niño/a(menor de 10)
# o pre-adolescente (edad entre 10 y 13 años) adolescente (edad entre 13 y 17 años) de edad.

edad = int(input("Ingrese su edad: "))
if edad > 0:
    if edad > 17:
        print("Es mayor de edad")
    elif edad < 10:
        print("Es un niño/a")
    elif edad < 14:
        print("Es pre-adolescente")
    elif edad < 18:
        print("Es adolescente")
else:
    print("Edad incorrecta")

print("Gracias por usar el programa!!!")