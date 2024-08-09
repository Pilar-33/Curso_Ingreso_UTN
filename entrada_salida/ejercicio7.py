from os import system
system("cls")
'''Ejercicio7: Tenemos que obtener el sueldo (por input) que el usuario nos ingrese , 
transformarlo en número entero y mostrar el importe de sueldo actualizado con 
el incremento del 15% utilizando print'''

incremento = 0.15
sueldo = int(input("Ingrese monto de su sueldo: $"))

importe_sueldo = sueldo * (1 + incremento)

print(f"Sueldo con incremento del 15%: ${importe_sueldo:.2f}")