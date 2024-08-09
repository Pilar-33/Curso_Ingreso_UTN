from os import system
system('cls')
'''Ejercicio3 Se deberá obtener tanto el nombre como la edad usando input 
y luego mostrar los datos concatenados con print. Ej: "Usted se llama José y su edad es 66 años" '''

name = input("Ingree su nombre: ")
age = int(input("ingrese su edad: "))

print(f"Usted se llama {name} y su edad es {age} años")