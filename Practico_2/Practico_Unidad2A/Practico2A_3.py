#3) Crear un programa que a partir del ingreso de la altura de un basquetbolista 
# determinar si es pivot o no. Para serlo el mismo deberá medir másde 1.80 metros.

altura = float(input("Por favor, la altura del basquetbolista en metros: "))

if altura > 1.80:
    print("Es un pivot")
else:
    print("No es un pivot")
print("Gracias!!!")