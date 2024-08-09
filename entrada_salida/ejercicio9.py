from os import system
system("cls")
'''Ejercicio9 Tenemos que crear un programa que deberá obtener el 
importe que ingrese el usuario por consola(input), transformar en número 
y mostrar el importe actualizado con un descuento del 20% utilizando print.'''

descuento = 20
importe = float(input("Ingrese el importe: $"))

importe_con_descuento = importe * (1 - (descuento/100))
print(f"El importe con descuento del {descuento}% es: ${importe_con_descuento:.2f}")

