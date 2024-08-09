from os import system
system("cls")
'''Ejercicio10 Tenemos que crear un programa que deberán obtener 
el importe y el descuento que ingrese el usuario por consola, 
transformarlos en números y mostrar el importe actualizado con el descuento utilizando print.'''

importe = float(input("Ingrese importe: $"))
descuento = int(input("Ingrese descuento (%): "))

importe_actualizado = importe * (1 - (descuento/100))
print(f"El importe con descuento del {descuento}% es: ${importe_actualizado:.2f}")