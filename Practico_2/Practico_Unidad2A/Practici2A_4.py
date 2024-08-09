#4) Crear un programa que se ingrese la edad del usuario en número y pueda calcular 
# si es adolescente (edad entre 13 y 17 años).

edad = int(input("Ingrese la edad del usurio: "))
if edad > 12 and edad < 18:
    print("Es adolescente")
else:
    print("No es adolescente")
print("Gracias por usar el programa!!!")