from os import system
system('cls')
#1) Crear un programa que pueda sumar los números pares comprendidos entre el 1 y el 10.

contador = 1
suma = 0
while contador < 11:
    if contador % 2 == 0:
        #suma = suma + contador
        suma += contador
    #contador = contador + 1
    contador += 1
print("La suma de los números pares entre 1 y el 10 es: ", suma)