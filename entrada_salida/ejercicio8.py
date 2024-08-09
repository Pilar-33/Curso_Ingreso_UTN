from os import system
system("cls")
'''Ejercicio8 Tenemos que obtener los valores (por input) que el 
usuario nos ingrese (sueldo e incremento), transformarlosennúmerosenteros 
y mostrar el importe de sueldo actualizado con el incremento porcentual utilizando print.'''

sueldo = float(input("Ingrese el monto de su sueldo: $"))
incremento = int(input("Ingrese incremento porcentual: "))

monto_imcremento = sueldo * (incremento/100)
sueldo_actualizado = sueldo + monto_imcremento

print(f"Sueldo actualizado con un incremento de {incremento}% es: ${sueldo_actualizado:.2f}" )