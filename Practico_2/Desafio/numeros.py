#Enunciado:
#Crear un programa que muestre en la consola 
#10 repeticiones con números ASCENDENTE desde el 1 al 10

print("=" * 25)
print("   NÚMEROS ASCENDENTES")
print("=" * 25)

number = 1
contador = 0

while number <= 10:
    if number == 10:
        print(number)
    else:
        print(f"{number}-", end="")
    number += 1
    contador += 1